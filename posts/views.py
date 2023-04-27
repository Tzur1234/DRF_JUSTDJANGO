from .serializers import PostSerializer
from rest_framework import generics
from .models import Post 
from .serializers import PostSerializer
# View to all posts (serialized)

from rest_framework.permissions import AllowAny, IsAuthenticated


from django.shortcuts import render

def home(request):
    return render(request=request, template_name='index.html')



class PostAPIView(generics.ListAPIView):
    permission_classes = (AllowAny ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
