from rest_framework import serializers

from member.serializers import UserSerializer
from post.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    # neasted relationship을 사용하여 comment를 참조함
    # read only 안하면 def create를 따로 선언해야함(보통 read only)
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'content',
        )


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'author',
            'content',
            'created_date',
        )


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'author',
            'content',
            'created_date'
        )