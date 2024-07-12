from rest_framework.viewsets import ModelViewSet

from .serializers import CommentSerializer,  PostDetailSerializer, PostListSerializer, LikeSerializer
from .models import Post, Comment, Like, PostImage
from posts.permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostListSerializer

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        images_data = self.request.FILES.getlist('images')
        for image_data in images_data:
            PostImage.objects.create(post=post, image=image_data)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrAdminOrReadOnly()]
        return []


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return Post.objects.get(pk=post_id)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdminOrReadOnly()]
        return super().get_permissions()


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post=self.get_post())

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return Post.objects.get(pk=post_id)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdminOrReadOnly()]
        return super().get_permissions()

