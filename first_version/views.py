from django.shortcuts import render, redirect
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
            # print(form.errors)
            # return HttpResponse('<script>alert("入力値が不正です")</script>')
            # return JsonResponse({'error': '入力が不正です。'})
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
    print("player_list:",type(player_list))
    
    return render(request, "first_version/list_players.html",{"player_list":player_list})




