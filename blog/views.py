from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post
from .models import Comment
from .forms import CommentForm
# Create your views here.


class StartPageView(ListView):
    template_name = 'blog/start_page.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'data'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def index(request): 
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     return render(request, 'blog/start_page.html', {
#         'data': latest_posts
#     })


class AllPostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    context_object_name = 'data'
    ordering = ['-date']


# def posts(request):
#     sorted_posts = Post.objects.all().order_by('-date')
#     return render(request, 'blog/posts.html', {
#         'data': sorted_posts
#     })


class PostDetailView(DetailView):
    template_name = 'blog/post_page.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tag.all()
        return context


# def post_id(request, post_id):
#     identified_post = get_object_or_404(Post, slug=post_id)
#     return render(request, 'blog/post_page.html', {
#         'post': identified_post,
#         'post_tags': identified_post.tag.all()
#     })


# class CommentForm(CreateView):
#     template_name = 'blog/post_page.html'
#     model = Comment
#     form_class = CommentForm
#     success_url = '/posts/<slug:post_id>'