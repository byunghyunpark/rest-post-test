from rest_framework import serializers

from post.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    # to_representation으로 photo_list에 comment_list 추가
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['comment_list'] = CommentSerializer(instance.comment_set.all(), many=True).data
        return ret


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
