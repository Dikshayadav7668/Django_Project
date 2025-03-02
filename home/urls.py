from django.contrib import admin
from django.urls import path,include
from home import views

# Django admin dashboard Customization
admin.site.site_header = "Login into the Dashboard"
admin.site.site_title = "Diksha Dashboard"
admin.site.site_index = "Welcome to the portfolio Dashboard"
admin.site.site_url = "http://127.0.0.1:8000/diksha"
urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path('projects',views.projects, name='projects'),
    path('contact', views.contact, name='contact')
]

