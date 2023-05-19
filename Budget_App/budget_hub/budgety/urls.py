from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mybudget", views.mybudget, name="mybudget"),
    path("connect", views.connect, name="connect"),
    path("login", views.login_view, name="login"),
    path("register", views.register_user, name="register_user"),
    path("logout_view", views.logout_view, name="logout_view"),
    path("add-expense",views.budgety,name="add-expense"),
    path("About", views.About, name="About"),
    path("contact", views.Contact, name="Contact"),
    path("Blog", views.Blog, name="Blog"),




]

