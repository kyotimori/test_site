from blog import views
from django.urls import path


urlpatterns = [
    path('', views.StartPageView.as_view(), name='index'),
    path('posts', views.AllPostsView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post_page')
]