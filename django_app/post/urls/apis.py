from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from post.apis import PostViewSet, CommentAPIView

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^(?P<post_pk>[0-9]+)/comment/$', CommentAPIView.as_view(), name='comment_list'),
    url(r'^(?P<post_pk>[0-9]+)/comment/add/$', CommentAPIView.as_view(), name='comment_add'),
]
