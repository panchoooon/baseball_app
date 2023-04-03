from django.shortcuts import render, redirect
from .models import players
from .forms import playerForm #forms.pyの内容を取ってくる。

from django.http import HttpResponse

#%%
# 能力値[750]に対してmark("B")を与える。
from django.db.models import IntegerField, Value

# メイン画面
def frontpage(request, *args, **kwargs): #urls.pyで定義した関数
  return render(request, 'prototype/frontpage.html') #renderは、描画する、の意味。

# 選手作成画面
def create_player(request):
  # 送信ボタンが押されたとき
  if request.method == "POST":
    print("if")
    form = playerForm(request.POST)
    print("form.",form)
    if form.is_valid():
      print("if→if")
      form.save()
      print("form.save()完了！！")
      return redirect('index')
    else:
      print("if→else")
      return redirect('create_player') #フォームの入力値が不正の場合、何もしない。

  else: 
    form = playerForm()
    return render(request, 'prototype/create_player.html', {"form":form})

#能力値に応じて、mark(能力値の目安を記号であらわしたもの)をつける。
def judge_mark(ability_value):
  ability_mark = "init"
  
  if 0 <= ability_value <= 299:
    ability_mark = "G"
  elif 300 <= ability_value <= 399:
    ability_mark = "F"
  elif 400 <= ability_value <= 499:
    ability_mark = "E"
  elif 500 <= ability_value <= 599:
    ability_mark = "D"
  elif 600 <= ability_value <= 699:
    ability_mark = "C"
  elif 600 <= ability_value <= 699:
    ability_mark = "C"
  elif 700 <= ability_value <= 799:
    ability_mark = "B"
  elif 800 <= ability_value <= 899:
    ability_mark = "A"
  elif 900 <= ability_value <= 1000:
    ability_mark = "S"
  else: ability_mark = "error!!"

  return ability_mark

# 750 → B750 といったアノテーション処理を行う。
def annotate(player_list):
  print("in:annotate")
  for player in player_list:
    player["contact"] = judge_mark(player["contact"]) + str(player["contact"])
    player["power"] = judge_mark(player["power"]) + str(player["power"])
    player["speed"] = judge_mark(player["speed"]) + str(player["speed"])
    player["handed"] = "右" if player["handed"] == "right" else ("左" if player["handed"] == "left" else "error!!")
    player["bbox"] = "右" if player["bbox"] == "right" else ("左" if player["bbox"] == "left" else "両")


  return player_list

def list_player(request):
  player_list = players.objects.all().values()
  player_list = annotate(player_list)
  
  return render(request, 'prototype/list_player.html',{"player_list":player_list}) #renderは、描画する、の意味。


def detail_player(request, id):
  player = players.objects.get(id=id)
  
  #450→E450といったアノテーション処理を行う。
  player.handed = "右" if player.handed == "right" else ("左" if player.handed == "left" else "error!!")
  player.bbox = "右" if player.bbox == "right" else ("左" if player.bbox == "left" else "両")
  player.contact = judge_mark(player.contact) + str(player.contact)
  player.power = judge_mark(player.power) + str(player.power)
  player.speed = judge_mark(player.speed) + str(player.speed)
  player.steeling = judge_mark(player.steeling) + str(player.steeling)
  player.arm_strength = judge_mark(player.arm_strength) + str(player.arm_strength)
  player.arm_accuracy = judge_mark(player.arm_accuracy) + str(player.arm_accuracy)
  player.catch = judge_mark(player.catch) + str(player.catch)
  player.reaction = judge_mark(player.reaction) + str(player.reaction)
  
  return render(request, 'prototype/detail_player.html',{"player":player}) #renderは、描画する、の意味。