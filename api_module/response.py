
from django.http import HttpResponse

class ResponseFormat() :

    def plusResposne(self, code, msg, data) :
        print(type(code))
        result =  {
                "statusCode" : code,
                "msg" : msg,
                "data" : data
            }
        print(result)
        return result
