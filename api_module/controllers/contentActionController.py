from rest_framework.views import APIView  
from Email_campaign_manager.models import PlusUserDetail
from api_module.response import ResponseFormat
from rest_framework.response import Response
from rest_framework import status  


class ContentAction(APIView) :
    def patch(self, request) :          #using patch since partial updation is done here
        user_id = request.GET.get('user_id', None)
        if not user_id :
            return Response(ResponseFormat().plusResposne(400, "MISSING_USER_ID", ""), status = status.HTTP_200_OK)
        try : 
            PlusUserDetail.objects.filter(id = user_id).update(isactive = 0)
            return Response(ResponseFormat().plusResposne(200, "DATA_SAVED", ""), status = status.HTTP_200_OK)
        except: 
            return Response(ResponseFormat().plusResposne(400, "DATA_NOT_SAVED", ""), status = status.HTTP_200_OK)
