from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/posts/', views.PostListView.as_view(), name='test1'),
    path('api/posts/<int:pk>/', views.PostDetailView.as_view(), name='test1'),
    path('api/posts/<int:pk>/delete/', views.PostDestroyView.as_view(), name='test1'),
    # path('api/posts/<pk>/', views.PostView.as_view(), name='test1'),
    # path('post_list/', views.post_list, name='test2'),
    # path('post_detail/<int:pk>/', views.post_detail, name='test3'),

]
