from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deploy.predict import ArticleGenerator
from article.models import Article
from article.serializers import ArticleSerializer
# Create your views here.

@api_view(['POST'])
def generate(request):
    content = request.data.get("content", None)
    model_type = request.data.get("model_type", None)
    if content is None:
        return Response(data = {"detail" : "lack of content"}, status = status.HTTP_400_BAD_REQUEST)
    if model_type is None:
        model_type = "policy"

    articleGenerator = ArticleGenerator(content)
    title = articleGenerator.generate_title(model_type).replace(" ",'')
    summary = articleGenerator.generate_summary()
    keyword_list = articleGenerator.generate_keywords()
    
    # title = "fake title"
    serialize_data = {  "title" : title, 
                        "content" : content,
                        "summary" : summary,
                        "keyword_list" : keyword_list}
    return Response(data=serialize_data, status=status.HTTP_200_OK)



from rest_framework.permissions import BasePermission

    
class IsAuthenticated(BasePermission):
    message = '仅登录用户可进行收藏操作'

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
        )


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        user = self.request.user
        queryset = queryset.filter(Q(author=user)).order_by('-created')
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
