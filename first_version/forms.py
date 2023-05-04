from django import forms

# モデルクラス
from .models import Player

# 選手フォーム
class PlayerForm(forms.ModelForm):
    
    class Meta():
      model = Player
      
      fields = \
      (
        ###############
        # プロフィール #
        ###############
        "lastName",
        "firstName",
        "career",
        "age",
        "number_of_years",
        "height",
        "weight",
        "uniformNumber",
        "birthPlace",
        "throw",
        "bbox",
        "player_type",
        "character",
        "profile",
        "image",
        ###########
        # 投手能力 #
        ###########
        "pitching_form",
        "stamina",
        "maximum_ball_speed",
        "power_of_straight",
        "growth_of_straight",
        "control_of_straight",
        "mental_strength",
        "strike_out",
        ###########
        # 野手能力 #
        ###########
        "contact",
        "power",
        "vision",
        "speed",
        "arm_strength",
        "arm_accuracy",
        "reaction",
        "catch",
        "main_position",
        "catcher_appropriate",
        "first_appropriate",
        "second_appropriate",
        "third_appropriate",
        "shortstop_appropriate",
        "left_appropriate",
        "center_appropriate",
        "right_appropriate",
        "chance",
        "vs_left_pitcher",
        "inside",
        "outside",
        "high_ball",
        "low_ball",
        "bunt",
        "base_running",
        "steeling",
        "pitcher_lead",
        "home_block",
        "sturdiness"
      )

    labels = \
      {
        ###############
        ##プロフィール##
        ###############
        "lastName":"姓",
        "firstName":"名",
        "career": "経歴",
        "age":"年齢",
        "number_of_years":"プロ年数",
        "height":"身長",
        "weight":"体重",
        "uniformNumber":"背番号",
        "birthPlace":"出身地",
        "throw":"利き腕",
        "bbox":"打席",
        "player_type":"選手タイプ",
        "character":"キャラクター",
        "profile":"プロフィール",
        ###########
        ##投手能力##
        ###########
        "pitching_form":"投球フォーム",
        "stamina":"スタミナ",
        "maximum_ball_speed":"最大球速",
        "power_of_straight":"ストレートの球威",
        "growth_of_straight":"ストレートのノビ",
        "control_of_straight":"ストレートのコントロール",
        "mental_strength":"メンタル",
        "strike_out":"奪三振",
        
        ###########
        ##野手能力##
        ###########
        "contact":"ミート",
        "power":"パワー",
        "vision":"選球眼",
        "speed":"走力",
        "arm_strength":"肩力",
        "arm_accuracy":"送球",
        "reaction":"打球反応",
        "catch":"捕球精度",
        "main_position":"メインポジション",
        "catcher_appropriate":"キャッチャー適正",
        "first_appropriate":"ファースト適正",
        "second_appropriate":"セカンド適正",
        "third_appropriate":"サード適正",
        "shortstop_appropriate":"ショート適正",
        "left_appropriate":"レフト適正",
        "center_appropriate":"センター適正",
        "right_appropriate":"ライト適正",
        "chance":"チャンス",
        "vs_left_pitcher":"対左投手",
        "inside":"インコース",
        "outside":"アウトコース",
        "high_ball":"ハイボール",
        "low_ball":"ローボール",
        "bunt":"バント",
        "base_running":"走塁",
        "steeling":"盗塁",
        "pitcher_lead":"投手リード",
        "home_block":"ブロック",
        "sturdiness":"ケガしにくさ"
        
      }

#選手プロフィール
# class PlayerProfileForm(forms.ModelForm):

#   class Meta():
#     model = Player
    
#     fields = \
#       (
#         ###############
#         # プロフィール #
#         ###############
#         "lastName",
#         "firstName",
#         "career",
#         "age",
#         "number_of_years",
#         "height",
#         "weight",
#         "uniformNumber",
#         "birthPlace",
#         "throw",
#         "bbox",
#         "player_type",
#         "character",
#       )
#     labels = \
#       {
#         ###############
#         ##プロフィール##
#         ###############
#         "lastName":"姓",
#         "firstName":"名",
#         "career": "経歴",
#         "age":"年齢",
#         "number_of_years":"プロ年数",
#         "height":"身長",
#         "weight":"体重",
#         "uniformNumber":"背番号",
#         "birthPlace":"出身地",
#         "throw":"利き腕",
#         "bbox":"打席",
#         "player_type":"選手タイプ",
#         "character":"キャラクター",
#         "profile":"プロフィール",
#       }

# #選手投手能力
# class PlayerPitcherForm(forms.ModelForm):
#   class Meta():
#     #モデルクラスを定義
#     model = Player
    
#     #表示するモデルクラスのフィールドを定義
#     fields = \
#       (
#         ###########
#         # 投手能力 #
#         ###########
#         "pitching_form",
#         "stamina",
#         "maximum_ball_speed",
#         "power_of_straight",
#         "growth_of_straight",
#         "control_of_straight",
#         "mental_strength",
#         "strike_out"
#       )
    
#     #表示ラベルを定義
#     labels = \
#       {
#         ###########
#         ##投手能力##
#         ###########
#         "pitching_form":"投球フォーム",
#         "stamina":"スタミナ",
#         "maximum_ball_speed":"最大球速",
#         "power_of_straight":"ストレートの球威",
#         "growth_of_straight":"ストレートのノビ",
#         "control_of_straight":"ストレートのコントロール",
#         "mental_strength":"メンタル",
#         "strike_out":"奪三振",
#       }
# #選手野手能力
# class PlayerFielderForm(forms.ModelForm):
  
#   class Meta():
#     #モデルクラスを定義
#     model = Player
    
#     #表示するモデルクラスのフィールドを定義
#     fields = \
#       (
#         ###########
#         # 野手能力 #
#         ###########
#         "contact",
#         "power",
#         "vision",
#         "speed",
#         "arm_strength",
#         "arm_accuracy",
#         "reaction",
#         "catch",
#         "main_position",
#         "catcher_appropriate",
#         "first_appropriate",
#         "second_appropriate",
#         "third_appropriate",
#         "shortstop_appropriate",
#         "left_appropriate",
#         "center_appropriate",
#         "right_appropriate",
#         "chance",
#         "vs_left_pitcher",
#         "inside",
#         "outside",
#         "high_ball",
#         "low_ball",
#         "bunt",
#         "base_running",
#         "steeling",
#         "pitcher_lead",
#         "home_block",
#         "sturdiness",
#       )
    
#     #表示ラベルを定義
#     labels = \
#       {
#       ###########
#       ##野手能力##
#       ###########
#         "contact":"ミート",
#         "power":"パワー",
#         "vision":"選球眼",
#         "speed":"走力",
#         "arm_strength":"肩力",
#         "arm_accuracy":"送球",
#         "reaction":"打球反応",
#         "catch":"捕球精度",
#         "main_position":"メインポジション",
#         "catcher_appropriate":"キャッチャー適正",
#         "first_appropriate":"ファースト適正",
#         "second_appropriate":"セカンド適正",
#         "third_appropriate":"サード適正",
#         "shortstop_appropriate":"ショート適正",
#         "left_appropriate":"レフト適正",
#         "center_appropriate":"センター適正",
#         "right_appropriate":"ライト適正",
#         "chance":"チャンス",
#         "vs_left_pitcher":"対左投手",
#         "inside":"インコース",
#         "outside":"アウトコース",
#         "high_ball":"ハイボール",
#         "low_ball":"ローボール",
#         "bunt":"バント",
#         "base_running":"走塁",
#         "steeling":"盗塁",
#         "pitcher_lead":"投手リード",
#         "home_block":"ブロック",
#         "sturdiness":"ケガしにくさ"
#       }