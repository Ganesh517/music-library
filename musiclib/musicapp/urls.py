from django.urls import path
from .views import *

urlpatterns = [
    # Album
    path('albums/', get_all_albhum),
    path('albums/create/', create_albhum),
    path('albums/<int:pk>/', get_album),
    path('albums/<int:pk>/update/', update_album),
    path('albums/<int:pk>/delete/', delete_album),
   

    # Song
    path('songs/', get_all_songs),
    path('songs/create/', create_song),
    path('songs/<int:pk>/', get_song),
    path('songs/<int:pk>/update/', update_song),
    path('songs/<int:pk>/delete/', delete_song),
    
]
