from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('artist/<int:pk>/', views.artist, name='artist'),
    path('artist/new/', views.artist_new, name='artist_new'),
    path('artist/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
]
