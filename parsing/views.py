from django.shortcuts import render
from django.views.generic.base import View
from . import models
from . import parse_vk


class PostId(View):
    """Пост по id"""
    def get(self, request, pk):
        post = models.Post.objects.get(id_from_vk=pk)
        return render(request, {"post": post})

class Down(View):
    """Пост по id"""
    def get(self, request):
        parse_vk.down()
        return render(request)
