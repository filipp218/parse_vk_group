from django.urls import path
from . import views

urlpatterns = [
    path("post/<int:pk>", views.PostId.as_view()),
    path("", views.AllPost.as_view()),
    path("date", views.DatePost.as_view()),
    path("date/<str:date>", views.DatePostGet.as_view()),
]
