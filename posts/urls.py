from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list/', views.PostAPIView.as_view(), name='post-list'),
    path('create/', csrf_exempt(views.CreatePostAPIView.as_view()), name='post-create'),
    path('detail/<int:pk>/', csrf_exempt(views.PostDetailAPIView.as_view()), name='post-detail'),
    path('update/<pk>/', csrf_exempt(views.PostUpdateView.as_view()), name='post-update'),
    path('delete/<pk>/', csrf_exempt(views.PostDeleteView.as_view()), name='post-update'),
    path('home/', views.home, name='home-test'),
]








