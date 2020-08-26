from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from news import views
from news.views import PostUpvoteView

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"posts", views.PostViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"upvotes", views.PostUpvoteViewSet)

API_AUTH = include("rest_framework.urls", namespace="rest_framework")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", API_AUTH),
    path("upvotes/<int:id>", PostUpvoteView.as_view(), name="post_upvotes"),
]
