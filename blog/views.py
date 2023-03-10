from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views import View

from .models import Post, Comment
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


class AllPostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    context_object_name = 'data'
    ordering = ['-date']


class PostDetailView(View):
    def get_data(self, request, slug):
        post = Post.objects.get(slug=slug)
        stored_posts = request.session.get('stored_posts')

        if stored_posts:
            is_saved_for_later = post.id in stored_posts
        else:
            is_saved_for_later = False

        data = {
            'post': post,
            'post_tags': post.tag.all(),
            'comment_form': CommentForm,
            'comments': post.comments.all().order_by('-date'),
            'is_stored': is_saved_for_later
        }
        return data

    def get(self, request, slug):
        return render(request, 'blog/post_page.html', self.get_data(request, slug))

    def post(self, request, slug):
        read_later_post = request.POST['post_id']
        request.session['read_later_posts'] = []
        request.session['read_later_posts'].append(read_later_post)

        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_page', args=[slug]))
    
        return render(request, 'blog/post_page.html', self.get_data(request, slug))
    

class StoredPostsView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['stored_posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['stored_posts'] = posts
            context['has_posts'] = True

        return render(request, 'blog/stored_posts.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id in stored_posts:
            stored_posts.remove(post_id)
        else:
            stored_posts.append(post_id)

        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect('/blog/')