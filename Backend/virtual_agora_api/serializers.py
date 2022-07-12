from rest_framework import serializers
from virtual_agora.models import Post
# Create your serializers here.


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'theme', 'author', 'description',
                  'status', 'published_date')
