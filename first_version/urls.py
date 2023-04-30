from django.urls import path
from first_version.views import create_player
from . import views

urlpatterns = [
    #選手作成画面
    path('create_player/', create_player, name="create_player"),
    
]