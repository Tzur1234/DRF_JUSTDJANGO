from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('posts', views.PostViewSet)

# Configure which methods allowed
post_detail = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
    # 'put': 'update'
})

urlpatterns = [
    path('', include(router.urls)),
    path('custom/', post_detail, name='custom')
]



