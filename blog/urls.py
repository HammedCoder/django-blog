from django.urls import path
from .views import BlogListView, BlogDetailView, PostCreateView, PostEditView, PostDeleteView


urlpatterns =[
    path('', BlogListView.as_view(), name='home'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name="edit_post"),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="delete_post"),
]