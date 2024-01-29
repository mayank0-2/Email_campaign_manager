from Email_campaign_manager.models import PlusUserDetail
from api_module.response import ResponseFormat
from rest_framework.views import APIView  
from rest_framework import status  
from rest_framework.response import Response
class userControllerFunction(APIView) :
    def post(self, request) :
        name_data = request.data.get('name')
        email_data = request.data.get('email')
        content_id_data = request.data.get('content_id')
        try :
            PlusUserDetail(name = name_data , email = email_data, content_id = content_id_data).save()
            return Response(ResponseFormat().plusResposne(200, "DATA_SAVED", ""), status = status.HTTP_200_OK)
        except :
            return Response(ResponseFormat().plusResposne(400, "DATA_NOT_SAVED", ""), status = status.HTTP_200_OK)
