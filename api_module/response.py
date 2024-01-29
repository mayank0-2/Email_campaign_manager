
from django.http import HttpResponse

class ResponseFormat() :

    def plusResposne(self, code, msg, data) :
        return {
                "statusCode" : {code},
                "msg" : {msg},
                "data" : {data}
            }
