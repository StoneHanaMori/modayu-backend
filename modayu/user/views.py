from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets, status, mixins
from django.contrib.auth.models import User
from rest_framework.response import Response
from serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = User.objects.all()
    lookup_field = 'username'
    lookup_value_regex = "[^/]+"
    serializer_class = UserSerializer

    def create(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        
        if username is None or password is None:
            return Response({"detail": "请提供完整的信息"}, status=status.HTTP_400_BAD_REQUEST)
        _user = User.objects.filter(username=username)
        if _user:
            return Response({"detail": "当前用户已经存在"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=username, password=password)
        user.set_password(password)
        user.save()
        return Response({"username": username}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @action(detail=False, methods=['patch'],
        url_path='password', url_name='password',
        permission_classes=[IsAuthenticated])
    def password(self, request, *args, **kwargs):
        user = request.user
        old_password = request.data.get("old_password", None)
        new_password = request.data.get("new_password", None)
        if old_password is None or new_password is None:
            return Response({"detail": "密码不能为空"}, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(old_password):
            return Response({"detail": "旧密码错误"}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({"detail": "修改成功"}, status=status.HTTP_200_OK)
