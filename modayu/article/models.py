from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import json

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="文章内容")
    summary = models.TextField(blank=True, verbose_name="摘要")
    created = models.DateTimeField(default=timezone.now)
    keyword_list = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='article_list'
    )

    def __str__(self):
        return self.title