from rest_framework import serializers

from .models import Post, PostImage



class PostDetailSerializerPhoto(serializers.ModelSerializer):
    """Фотографии"""

    class Meta:
        model = PostImage
        fields = ("photo",)

class PostDetailSerializerData(serializers.ModelSerializer):
    """Текстовая часть поста"""
    images = PostDetailSerializerPhoto(many=True)

    class Meta:
        model = Post
        fields = ("id", "text", "date_of_post", "vk_id", "url", "images")



