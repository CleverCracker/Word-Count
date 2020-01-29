from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('count/', views.Count, name='count'),
    path('about/', views.About, name='about'),
]
