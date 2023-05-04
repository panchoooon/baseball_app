from django.urls import path
from first_version.views import create_player, list_players
from . import views

urlpatterns = [
    #選手作成画面
    path('create_player/', create_player, name="create_player"),
    #選手一覧画面
    path('list_player/', list_players, name="list_players"),
    
]