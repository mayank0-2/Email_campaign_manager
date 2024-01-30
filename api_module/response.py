
from django.http import HttpResponse

class ResponseFormat() :

    def plusResposne(self, code, msg, data) :
        result =  {
                "statusCode" : code,
                "msg" : msg,
                "data" : data
            }
        return result
        