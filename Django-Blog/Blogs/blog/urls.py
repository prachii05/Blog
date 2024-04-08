from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogpost/", views.blogpost, name="blogpost"),
    path("search/", views.search, name="search"),
    path('contact/', views.contact, name='contact'),
    path('blogg/', views.blogg, name='blogg'),
    
]
