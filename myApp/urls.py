from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "Apni Shop Admin"
admin.site.site_title = "Apni Shop Admin Portal"
admin.site.index_title = "Welcome to Apni Shop"
urlpatterns = [

    path('', views.index,name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]