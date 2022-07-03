from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deploy.predict import ArticleGenerator
# Create your views here.

@api_view(['POST'])
def generate(request):
    body = request.data.get("content", None)
    if body is None:
        return Response(data = {"detail" : "lack of content"}, status = status.HTTP_400_BAD_REQUEST)
    abstract = ArticleGenerator(body).generate().replace(" ",'')
    # abstract = "fake abstract"
    title = "fake title"
    serialize_data = {  "title" : title, 
                        "body" : body,
                        "abstract" : abstract}
    return Response(data=serialize_data, status=status.HTTP_200_OK)
