from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import add_song

app_name = "App"

urlpatterns = [
    path("", views.index, name="index"),
    path('/<int:song_id>/', views.song_detail, name='song_detail'),
    path('add/', add_song, name='add_song'),
]
