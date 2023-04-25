from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostAPIView.as_view(), name='post-list'),
    path('home', views.home, name='home-test'),
]
