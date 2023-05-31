from django.urls import path
from first_version.views import top, create_player, list_players, detail_player
from . import views

urlpatterns = [
    #選手作成画面
    path('create_player/', create_player, name="create_player"),
    
    #選手一覧画面
    path('list_player/', list_players, name="list_players"),
    
    #選手詳細画面
    path('detail/<int:player_id>',detail_player, name="detail_player"),
]