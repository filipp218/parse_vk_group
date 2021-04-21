from .models import Post, PostImage
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostDetailSerializer,PostDetailSerializerData
from .paginate import paginate


class PostListView(APIView):
    """вывод списка постов"""

    def get(self, request):
        posts = Post.objects.all()
        context = paginate(request, posts)
        serializer = PostDetailSerializerData(context, many=True)
        return Response(serializer.data)


    def post(self, request):
        """вывод постов по дате"""
        date = request.POST.get("calendar")
        if date:
            posts = Post.objects.filter(date_of_post=date)
            context = paginate(request, posts)
            serializer = PostDetailSerializerData(context, many=True)
            return Response(serializer.data)
        return Response(404)

class PostDetailView(APIView):
    """детальный вывод поста"""
    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            photos = PostImage.objects.filter(post=post)
            filter = {}
            filter['post'] = post
            filter['photos'] = photos
            serializer = PostDetailSerializer(filter)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(404)




