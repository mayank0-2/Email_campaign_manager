
from Email_campaign_manager.models import PlusUserDetail, PlusContent
from rest_framework.views import APIView  
from rest_framework.response import Response

class ContentControllerFunction(APIView) :
    def post(self, request) :
        #add validators for both 
        content = request.data.get('content')
        content_id = request.data.get('content_id')
        try :
            PlusContent(content = content, content_id = content_id).save()
            return Response(ResponseFormat().plusResposne(200, "DATA_SAVED", ""), status = status.HTTP_200_OK)
        except :
            return Response(ResponseFormat().plusResposne(400, "DATA_NOT_SAVED", ""), status = status.HTTP_200_OK)


