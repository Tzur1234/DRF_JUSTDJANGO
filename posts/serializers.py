from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField()
    id = serializers.HyperlinkedRelatedField(view_name='post-detail', many=False, read_only=True)
    hyper_link = serializers.HyperlinkedRelatedField(view_name='post-detail', many=False, read_only=True)
    class Meta:
        model = Post
        fields = ('title', 'content', 'publish_date', 'last_updated', 'author','id','hyper_link')
    
    # def get_author(self, obj):
    #     # return the name of the author
    #     return obj.author.user.username
    

class PostCreateSerializer(serializers.ModelSerializer):
        id = serializers.SerializerMethodField()
        class Meta:
            model = Post
            fields = ('title', 'content', 'author', 'id' , )

        def get_id(self, obj):
            # return the name of the author
            return obj.id
    