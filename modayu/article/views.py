from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize
# Create your views here.

@api_view(['POST'])
def generate(request):
    body = request.data.get("body", None)
    if body is None:
        return Response(data = {"detail" : "lack of body"}, status = status.HTTP_400_BAD_REQUEST)
    title = "fake title"
    abstract = "fake abstract"
    serialize_data = {  "title" : title, 
                        "body" : body,
                        "abstract" : abstract}
    return Response(data=serialize_data, status=status.HTTP_200_OK)
