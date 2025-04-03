from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_player, name='register'),
    path('update-highscore/', views.update_highscore, name='update_highscore'),
    path('player/<str:username>/', views.get_player, name='get_player'),
    path('all/', views.get_all_players, name='get_all_players'),
]