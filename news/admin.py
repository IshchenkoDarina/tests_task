from django.contrib import admin
from .models import Post, Comment
from .models.post import PostUpvote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    # list_display = ('title', 'creation_date', '', 'author')
    search_fields = ("title",)


@admin.register(PostUpvote)
class PostUpvoteAdmin(admin.ModelAdmin):
    pass
    # list_display = ('post', 'author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
    # list_display = ('author', 'post', 'creation_date', 'content')
