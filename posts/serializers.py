from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('title', 'content', 'publish_date', 'last_updated', 'author', )
    
    def get_author(self, obj):
        # return the name of the author
        return obj.author.user.username