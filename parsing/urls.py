from django.urls import path
from . import views

urlpatterns = [
    path("post/<int:pk>", views.PostDetailView.as_view()),
    path("post/", views.PostListView.as_view()),
]
