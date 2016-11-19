from rest_framework import serializers

from post.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # neasted relationship을 사용하여 comment를 참조함
    # read only 안하면 def create를 따로 선언해야함(보통 read only)
    comment_list = CommentSerializer(many=True, read_only=True, source='comment_set')

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'content',
            'comment_list'
        )

    # to_representation으로 photo_list에 comment_list 추가
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # ret['comment_list'] = CommentSerializer(instance.comment_set.all(), many=True).data
        return ret
