from rest_framework import permissions
from rest_framework import viewsets

from post.models import Post
from post.permissions import IsOwnerOrReadOnly
from post.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
