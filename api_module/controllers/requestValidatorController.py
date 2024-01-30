from functools import wraps

def isValidRequest(f) :
    @wraps(f)
    def validate(*args, **kwargs) :
        request_obj = request.data
        if request.path == '/api/EnterUserData' :
            name_data = request_obj.get('name', None)
            email_data = request_obj.get('email', None)
            content_id_data = request_obj.get('content_id', None)
            if not name_data or not email_data or not content_id_data :
                return Response(ResponseFormat().plusResposne(400, "INVALID_DATA", ""), status = status.HTTP_200_OK)
        
        elif request.path == '/api/EnterUserContent' :
            content_data = request_obj.get('content', None)
            content_id_data = request_obj.get('content_id', None)
            if not content_data or not content_id_data :
                return Response(ResponseFormat().plusResposne(400, "INVALID_DATA", ""), status = status.HTTP_200_OK)
        
        elif request.path == '/api/Unsubscribe' :
            user_id_data = request_obj.get('user_id', None)
            if not user_id_data :
                return Response(ResponseFormat().plusResposne(400, "INVALID_DATA", ""), status = status.HTTP_200_OK)

        


        return f(*args, **kwargs)
    return validate