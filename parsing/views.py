from .models import Post
from .serializers import PostDetailSerializerData
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .service import PostFilter

class PostListView(ListAPIView):
    """вывод списка постов"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializerData
    filter_backends = (DjangoFilterBackend,)
    filter_class = PostFilter

class PostDetailView(RetrieveAPIView):
    """детальный вывод поста"""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializerData




