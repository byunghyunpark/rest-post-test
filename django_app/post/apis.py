from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from post.models import Post, Comment
from post.permissions import IsOwnerOrReadOnly
from post.serializers import PostSerializer, CommentSerializer


# ModelViewSet으로 구현
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# APIView로 구현
class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            post = get_object_or_404(Post, pk=kwargs.get('pk'))
            comments = Comment.objects.filter(post=post)
        else:
            comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, *args)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
