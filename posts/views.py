from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser # Use to parse incoming HttpRequest into Python Data
from rest_framework.renderers import JSONRenderer #a built-in renderer in Django Rest Framework that serializes data into JSON format.
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


from .models import Post
from .serializers import PostSerializer


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse



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
        


        


        

    
   

