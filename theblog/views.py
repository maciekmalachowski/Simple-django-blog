from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    # fields = '__all__'
    fields = ('title', 'text')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
