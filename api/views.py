from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, CreatePostSerializer
from django.http import Http404, HttpResponse
from .models import Post

class ViewPosts(APIView):
    
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

class PostDetails(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

# search for posts ....
class FindPosts(APIView):
    # filter tags for keyword
    def get(self, request, format=None):
        query = request.GET.get('q', None)
        posts = Post.objects.filter(pk=query)
        serializer = CreatePostSerializer(posts, many=True)
        return Response(serializer.data)
