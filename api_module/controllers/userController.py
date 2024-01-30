from Email_campaign_manager.models import PlusUserDetail
from api_module.response import ResponseFormat
from rest_framework.views import APIView  
from rest_framework import status  
from rest_framework.response import Response
from api_module.controllers.kafkaController import KafkaProducer
from config import ConfigVariables


class userControllerFunction(APIView) :
    def post(self, request) :
        #add validators
        name_data = request.data.get('name')
        email_data = request.data.get('email')
        content_id_data = request.data.get('content_id')
        PlusUserDetail(name = name_data , email = email_data, content_id = content_id_data).save()
        KafkaProducer().producer_message(ConfigVariables().topic_name_for_kafka, ConfigVariables().message_for_kafka) #derive these from config
        try :
            return Response(ResponseFormat().plusResposne(200, "DATA_SAVED", ""), status = status.HTTP_200_OK)
        except :
            return Response(ResponseFormat().plusResposne(400, "DATA_NOT_SAVED", ""), status = status.HTTP_200_OK)


