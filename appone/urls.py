from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("review/", views.review, name="review"),
    path("prep/", views.prep, name="prep"),
    path("email/", views.email_signup, name="email_signup")
]