from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import permissions

from .serializers import (
    UserSerializer,
    PostSerializer,
    PostUpvoteSerializer,
    CommentSerializer,
)
from .models import Post, Comment
from .models.post import PostUpvote
from rest_framework.exceptions import ValidationError


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(ModelViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user.username)


class PostUpvoteViewSet(ModelViewSet, RetrieveUpdateDestroyAPIView):
    queryset = PostUpvote.objects.all()
    serializer_class = PostUpvoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = serializer.validated_data["post"]
        user = self.request.user
        if PostUpvote.objects.filter(author=user, post=post).count() == 0:
            serializer.save(author=user)

            post.amount_of_upvotes += 1
            post.save()
        else:
            raise ValidationError()


class PostUpvoteView(CreateAPIView):
    queryset = PostUpvote.objects.all()
    serializer_class = PostUpvoteSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author_name=user.username)
