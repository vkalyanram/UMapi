from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt

def get_data(var:str):
    SECRET_KEY = "python_jwt"
    token =var
    try:
        decode_data = jwt.decode(jwt=token, \
                            key=SECRET_KEY, algorithms="HS256")
        return decode_data
    except Exception as e:
        message = f"Token is invalid --> {e}"
        return message
       

@api_view(['GET'])
def get_details(request,token_value):
	details=get_data(token_value)
	return Response(details)
