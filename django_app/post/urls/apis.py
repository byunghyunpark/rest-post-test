from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from post.apis import PostViewSet, CommentView

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
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^(?P<pk>[0-9]+)/comment/$', CommentView.as_view(), name='comment'),
]
