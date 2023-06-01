from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #ログイン必須の画面で使う
from django.contrib import messages
# Create your views here.
# from .forms import PlayerProfileForm, PlayerPitcherForm, PlayerFielderForm
from .forms import PlayerForm
from .models import Player
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.http import JsonResponse

import json
from django.db.models import QuerySet
import pandas as pd

position_map = {
    "pitcher":"投手",
    "catcher":"捕手",
    "first":"内野手",
    "second":"内野手",
    "third":"内野手",
    "shortstop":"内野手",
    "left":"外野手",
    "center":"外野手",
    "right":"外野手"
}

# トップ画面
def top(request):
    return render(request, "first_version/top.html")

# 選手作成画面
@login_required
def create_player(request):
    if request.method == "POST":
        print("views.py:if request.method == 'POST':")
        print("--------------------------------------------------------------")
        
        form = PlayerForm(request.POST, request.FILES)
        
        # フォームの入力内容がすべて有効である場合、モデルへの保存処理を実行する。
        if form.is_valid():
            print("form.is_valid()True")
            player = form.save(commit=False)
            player.created_by = request.user #入力フォームには存在しない、作成者(ログインユーザーとする)の情報を入れる
            player.save()
            return render(request, "first_version/top.html")
        else:
            print("views.py:POST/else(ERROR)")
            print("----------------------------------------------------------")
            messages.error(request, "不正な入力があります")
            return render(request, "first_version/create_player.html", \
                {"form": form})

    else:
        print("views.py:in(else)")
        form = PlayerForm()
        # print(form.fields.keys())
        target_keys = ( #投手能力
                        "stamina","power_of_straight","growth_of_straigh","power_of_straigh","mental_strength","strike_out",
                        #野手能力
                        "contact", "power", "vision", "speed", "arm_strength", "arm_accuracy", "reaction", "catch", "chance", "vs_left_pitcher"\
                        "inside", "outside", "high_ball", "low_ball","bunt","base_running","steeling","pitcher_lead","home_block","sturdiness")
        keys = list(form.fields.keys())
        values = ["D" for i in range(len(keys))]
        # keys = [k for k in keys if k in target_keys]
        abilities_dict = dict(zip(keys, values))
        # print(f"abilities_dict:{abilities_dict}")
        
        return render(request, "first_version/create_player.html", \
            {"form": form, "abilities_dict":abilities_dict})


# 選手一覧画面
def list_players(request):
    player_list = Player.objects.all().values() #DBから選手データを取り出し

    
    # df = pd.DataFrame(player_list)
    # print("type(player_list):",type(player_list))
    # # 「ファースト...ショート」→「内野手」のように値をマッピング
    # df["main_position_roughly"] = df["main_position"].map(position_map)
    # # print("df.to_json():",df.to_json())
    # print("type(df.to_json):",type(df.to_json()))
    # json_list = json.loads(df.to_json())
    # queryset = QuerySet(model=Player, query=None, objects=json_list)
    # player_list = df.to_json()
    return render(request, "first_version/list_players.html",{"player_list":player_list})

def get_rough_position(position):
    
    rough_position = None #初期化
    if position == "pitcher":
        rough_position = "投手"
    elif position == "catcher":
        rough_position = "捕手"
    elif position in ("first","second","third","shortstop"):
        rough_position = "内野手"
    elif position in ("left","center","center"):
        rough_position = "外野手"
    else: rough_position = "ERROR"
    return rough_position

# 選手詳細画面
def detail_player(request, player_id):
    player = Player.objects.get(player_id=player_id) #DBから選手データを取り出し

    fielderAbility = {
        "data":[player.contact,player.power,player.vision,\
                player.speed,player.arm_strength,\
                player.arm_accuracy,player.reaction,player.catch]
    }
    context = {
        "fielderAbility":fielderAbility,
        "player":player
    }
    # サード→内野手。のように大まかなポジションの値を取得する。
    player.main_position = get_rough_position(player.main_position)
    # return render(request, 'first_version/detail_player.html',{"player":player}) #renderは、描画する、の意味。
    return render(request, 'first_version/detail_player.html',context) #renderは、描画する、の意味。

    

