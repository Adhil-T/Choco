from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("chocolate", views.chocolate, name="chocolate"),
    path("testimonial", views.testimonial, name="testimonial"),
    path("login", views.login1, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout1, name="logout")
]