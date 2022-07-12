from django.urls import path
from .views import PostList, PostDetail

app_name = 'virtual_agora_api'

urlpatterns = [
    path('posts', PostList.as_view(),name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(),name='post_detail'),
]
