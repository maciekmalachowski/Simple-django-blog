from django.urls import path
from .views import IndexView, PostDetailView, AddPostView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
]
