from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deploy.predict import ArticleGenerator
from article.models import Article
from article.serializers import ArticleSerializer
import json
# Create your views here.

@api_view(['POST'])
def generate(request):
    content = request.data.get("content", None)
    model_type = request.data.get("model_type", None)
    if content is None:
        return Response(data = {"detail" : "lack of content"}, status = status.HTTP_400_BAD_REQUEST)
    articleGenerator = ArticleGenerator(content)
    title = articleGenerator.generate_title(model_type).replace(" ",'')
    summary = articleGenerator.generate_summary()
    keywords = articleGenerator.generate_keywords()
    
    serialize_data = {  "title" : title, 
                        "content" : content,
                        "summary" : summary,
                        "keywords" : keywords}
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

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        keywords = data.get("keywords", None)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        if keywords is not None:
            keywords = json.dumps(keywords)
            serializer.save(keywords=keywords)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = request.data.copy()
        keywords = data.get("keywords", None)
        if keywords is not None:
            keywords = json.dumps(keywords)
            serializer.save(keywords=keywords)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
