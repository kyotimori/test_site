from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def index(request): 
    intro = 'Hiiiiii this is my blog!'
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/start_page.html', {
        'intro': intro,
        'data': latest_posts
    })


def posts(request):
    sorted_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/posts.html', {
        'data': sorted_posts
    })


def post_id(request, post_id):
    identified_post = get_object_or_404(Post, slug=post_id)
    return render(request, 'blog/post_page.html', {
        'post': identified_post,
        'post_tags': identified_post.tag.all()
    })
