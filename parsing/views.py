from django.shortcuts import render, redirect
from .models import Post, PostImage
from .paginate import paginate
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostListSerializer, PostDetailSerializer, PostDetailSerializerPhoto
from .paginate import paginate

class PostListView(APIView):
    """вывод списка постов"""
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    """вывод списка постов"""
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        photos = PostImage.objects.filter(post=post)
        filter = {}
        filter['post'] = post
        filter['photos'] = photos
        serializer_photo = PostDetailSerializerPhoto(filter)
        return Response(serializer_photo.data)





# class PostId(View):
#     """Пост по id"""
#
#     def get(self, request, pk):
#         post = models.Post.objects.get(id=pk)
#         post_image = post.images.all()
#         context = {}
#         context["post"] = post
#         if post_image:
#             context["post_image"] = post_image
#         return render(request, "main/post.html", context)


# class AllPost(ListView):
#     """Все посты"""
#
#     def get(self, request):
#         posts = models.Post.objects.all()
#         context = paginate.paginate(request, posts)
#         return render(request, "main/all_posts.html", context)
#
#
# class DatePostGet(View):
#     """Посты по дате"""
#
#     def get(self, request, date):
#         posts = models.Post.objects.filter(date_of_post=date)
#         context = paginate.paginate(request, posts)
#         return render(request, "main/all_posts.html", context)
#
#
# class DatePost(View):
#     """Принимает дату для фильтрации"""
#
#     def post(self, request):
#         date = request.POST.get("calendar")
#         if date:
#             return redirect(f"date/{date}")
#         return redirect("/")
