from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment
from .models.post import PostUpvote


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "link", "author_name", "amount_of_upvotes"]
        read_only_fields = ("author_name", "amount_of_upvotes")


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["author_name", "post", "creation_date", "content"]
        read_only_fields = ("author_name", "creation_date")


class PostUpvoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostUpvote
        fields = ["post", "author"]
        read_only_fields = ("author",)
