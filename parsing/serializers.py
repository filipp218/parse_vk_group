from rest_framework import serializers

from .models import Post, PostImage


class PostListSerializer(serializers.ModelSerializer):
    """Список постов"""

    class Meta:
        model = Post
        fields = ("text", "date_of_post", "vk_id", "url")


class PostDetailSerializer(serializers.ModelSerializer):
    """Один пост"""

    class Meta:
        model = PostImage
        fields = ("photo",)


class PostDetailSerializerPhoto(serializers.Serializer):
    """Картинки поста"""
    post = PostListSerializer(read_only=True)
    photos = PostDetailSerializer(read_only=True, many=True)

