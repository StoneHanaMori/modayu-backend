from rest_framework import serializers
from article.models import Article
from rest_framework.serializers import SerializerMethodField
import json

class ArticleSerializer(serializers.ModelSerializer):
    keywords = SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'summary',
            'content',
            'author',
            'keywords',
            'created'
        ]
    
    def get_keywords(self, instance):
        if instance.keywords != "" : 
            return json.loads(instance.keywords)
        return []