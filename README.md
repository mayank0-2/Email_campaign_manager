# Email_campaign_manager
This project consists of an Email Campaign Manager

Database structure : 
  We have two database tables which store the data for the newsletter named plus_user_detail and plus_content where in plus_user_detail we store the basic info of the user which consists of storing the email, name, consent of the user and also it contains a foreign key which maps the user to the content in the Plus_content table this structure of database helps us to avoid the storage of redundant data for multiple users.

Optimisation : 
  I have used Kafka and celery for the optimisation of the overall process as at first I used a Kafka producer to map the content of the user and push it to the Kafka and created a consumer to poll the data and push this data for processing into the celery queue which will then send the email and in the mean time the Kafka consumer is polling data for another user.
