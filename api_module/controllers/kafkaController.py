from Email_campaign_manager.models import PlusUserDetail, PlusContent
import socket, json
from confluent_kafka import Producer, Consumer
from api_module.controllers.emailerController import send_email
from rest_framework.views import APIView

class KafkaProducer :
    def __init__(self):
        conf = {'bootstrap.servers': "localhost:9092", 'client.id': socket.gethostname() }
        self.producer = Producer(conf)
    
    def producer_message(self, topic, message) :
        user_data = PlusUserDetail.objects.all()
        for row in user_data :
            id = row.id
            name = row.name
            email = row.email
            content_id = row.content_id
            content = PlusContent.objects.get(content_id = content_id).content
            message = {
                'id' : id, 
                'name' : name,
                'email' : email,
                'content' : content
            }
            print(message)
            self.producer.produce(topic, key = None, value = json.dumps(message))
            # self.producer.flush()
        self.producer.close()



class KafkaConsumer :
    def __init__(self) :
        self.conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'foo','auto.offset.reset': 'smallest'}
        self.consumer = Consumer(conf)
    
    def consumer_message(self, topic) :
        self.consumer.subscribe([topic])
        while True :
            msg = self.consumer.poll(1.0)
            if msg is None :
                continue
            if msg.error() :
                print("Consumer error: {}".format(msg.error()))
                continue
            message = msg.value().decode('utf-8')
            send_email.delay(message)
            self.consumer.close()


class exposeEndpoint(APIView):
    def get(self, request) :

        KafkaProducer().producer_message("test", "test")
        KafkaConsumer().consumer_message("test")

        return Response(ResponseFormat().plusResposne(200, "STAGING_STARTED", ""), status = status.HTTP_200_OK)