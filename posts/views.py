from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser # Use to parse incoming HttpRequest into Python Data
from rest_framework.renderers import JSONRenderer #a built-in renderer in Django Rest Framework that serializes data into JSON format.
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerPermission
from rest_framework import viewsets

from .models import Post, Comment
from .serializers import PostSerializer, UserSerializer, CommentSerializer


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


from django.contrib.auth import get_user_model
User = get_user_model()

class CommentListView(generics.ListAPIView):
    # returns all the comments
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveAPIView):
    # returns all the comments
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserDetailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer



class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, IsAuthenticated, IsOwnerPermission,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostMixinsListView(mixins.ListModelMixin ,
                          mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # use the create() to take care of the : 
        # 1. make from the request.data a new serializer instance 
        # 2. validate the serializer
        # 3. Save the new instance in the DB
        # 4. Generate a new Response object 
        return self.create(request=request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        # Use the update() from UpdateModelMixin to update the mixins
        # 1. get the object from the db according to the pk in the url
        # 2. Create a serializer based on the new request.data and the older instance 
        # 3. Check if is_vlaid()
        # 4. if vlaid , update the db (serializer.save())
        # 4. return a response (serializer.data)
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        # use destroy function from mixins.DestroyModelMixin to delete
        # 1. fetch the instance 
        # 2. delte it from the db
        # 3. send back a Response object
        return self.destroy(request, *args, **kwargs)


    

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == "GET":
        pass




class PostView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):

        queryset = Post.objects.all()
        serializer= PostSerializer(queryset, many=True) #Passing many serializers

        # return Response Object
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save the data in the db
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk ,*args, **kwargs):
        # check if the current id exists
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)
              
        serializer = PostSerializer(post, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk ,*args, **kwargs):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)
        
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)
         

@csrf_exempt
def post_list(request):
    
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True) #serialize the all posts
        return JsonResponse(serializer.data, safe=False)
    

    if request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = PostSerializer(data=data)

        # Vlidate the incoming data
        if serializer.is_valid():
            # send ok response 
            return JsonResponse(data=serializer.data, safe=False, status=201)
        else:
            return JsonResponse(data=serializer.errors, safe=False, status=400)
        

@csrf_exempt
def post_detail(request, pk):
    # Vlidate the instace exists
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        data = JSONParser(request)
        serializer = PostSerializer(post ,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,safe=False, status=201)
        else:
            return JsonResponse(data=serializer.error, safe=False ,status=400)
        
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse('Object was deleted!' ,status=204)
        

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

        


        

    
   

