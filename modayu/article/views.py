from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deploy.predict import ArticleGenerator
# Create your views here.

@api_view(['POST'])
def generate(request):
    content = request.data.get("content", None)
    if content is None:
        return Response(data = {"detail" : "lack of content"}, status = status.HTTP_400_BAD_REQUEST)
    # summary = ArticleGenerator(content).generate().replace(" ",'')
    summary = "fake abstract"
    title = "fake title"
    serialize_data = {  "title" : title, 
                        "content" : content,
                        "summary" : summary}
    return Response(data=serialize_data, status=status.HTTP_200_OK)
