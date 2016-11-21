import json

import generic as generic
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import MyUser
from post.models import Post, Comment
from post.permissions import IsOwnerOrReadOnly
from post.serializers import CommentSerializer, CommentListSerializer
from post.serializers import PostSerializer

User = get_user_model()


# ModelViewSet으로 구현
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# APIView로 구현
class CommentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(post=kwargs.get('post_pk'))
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs.get('post_pk'))
        author = MyUser.objects.get(id=request.user.pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['post'] = post
            serializer.validated_data['author'] = author
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
