from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

# Create User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)



class PostSerializer(serializers.ModelSerializer):
    # connect the owner field to post's owner
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', many=False, read_only=True)
    comment = serializers.HyperlinkedRelatedField(view_name='comment-detail', many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ('title', 'custom_id', 'category', 'publish_date', 'last_updated', 'owner', 'comment' ,)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title',)


