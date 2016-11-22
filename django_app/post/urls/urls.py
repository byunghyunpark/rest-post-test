from django.conf.urls import url

from post.views import PostList, PostDetail, PostAdd

urlpatterns = [
    url(r'^post/$', PostList.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/', PostDetail.as_view(), name='post_detail'),
    url(r'^post/add/$', PostAdd.as_view(), name='post_add')
]