from django.shortcuts import render
from .models import Post


class PostId(View):
    """Пост по id"""
    def get(self, request, pk):
        post = Post.objects.get(id_from_vk=pk)
        return render(request,  {"post": post})

