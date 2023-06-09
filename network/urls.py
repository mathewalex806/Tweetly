
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post , name="new_post"),
    path("profile/<str:username>", views.profile, name= "profile"),
    path("following", views.following , name= "following"),
    path("follow_unfollow", views.follow_unfollow , name= "follow_unfollow"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("add_like/<int:post_id>", views.add_like, name="add_like"),
    path("remove_like/<int:post_id>", views.remove_like, name="remove_like"),
]
