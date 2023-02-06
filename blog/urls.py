from blog import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('posts/<slug:post_id>', views.post_id, name='post_page')
]