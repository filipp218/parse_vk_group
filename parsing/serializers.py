from rest_framework import serializers

from .models import Post, PostImage


class PostDetailSerializerData(serializers.ModelSerializer):
    """Текстовая часть поста"""

    class Meta:
        model = Post
        fields = ("id", "text", "date_of_post", "vk_id", "url")


class PostDetailSerializerPhoto(serializers.ModelSerializer):
    """Фотографии"""

    class Meta:
        model = PostImage
        fields = ("photo",)


class PostDetailSerializer(serializers.Serializer):
    """Детали поста"""
    post = PostDetailSerializerData(read_only=True)
    photos = PostDetailSerializerPhoto(read_only=True, many=True)

