from django.shortcuts import render
from rest_framework import generics
from virtual_agora.models import Post
from .serializers import PostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
