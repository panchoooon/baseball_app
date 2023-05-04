from django.shortcuts import render, redirect

# Create your views here.
# from .forms import PlayerProfileForm, PlayerPitcherForm, PlayerFielderForm
from .forms import PlayerForm
from .models import Player
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
# トップ画面
def top(request):
    return render(request, "first_version/top.html")


# 選手作成画面
def create_player(request):
    if request.method == "POST":
        print("views.py:if request.method == 'POST':")
        print("----------------------------------------------------------")
        
        form = PlayerForm(request.POST, request.FILES)
        
        # フォームの入力内容がすべて有効である場合、モデルへの保存処理を実行する。
        if form.is_valid():
            print("form.is_valid()True")
            player = form.save(commit=False)
            # player.created_by = request.user
            player.save()
            return render(request, "first_version/top.html")
        else:
            print("views.py:POST/else(ERROR)")
            print("----------------------------------------------------------")
            print(form.errors)
            
    else:
        form = PlayerForm()
    
    return render(request, "first_version/create_player.html", \
                    {"form":form})



