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
        # "player_type",
        "character",
        "image",
        "profile",
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
        
        #変化球#
        "flg_slider","power_of_slider","breaking_of_slider","control_of_slider","change_amount_of_slider",
        "flg_curve","power_of_curve","breaking_of_curve","control_of_curve","change_amount_of_curve",
        "flg_fork","power_of_fork","breaking_of_fork","control_of_fork","change_amount_of_fork",
        "flg_sinker","power_of_sinker","breaking_of_sinker","control_of_sinker","change_amount_of_sinker",
        "flg_shoot","power_of_shoot","breaking_of_shoot","control_of_shoot","change_amount_of_shoot",
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
        "pitcher_appropriate",
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
        # "player_type":"選手タイプ",
        "main_position":"メインポジション",
        "character":"キャラクター",
        "image":"見た目",
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
        
        #スライダー
        "flg_slider":"スライダーの有無",
        "power_of_slider":"スライダーの球威",
        "breaking_of_slider":"スライダーのキレ",
        "control_of_slider":"スライダーのコントロール",
        "change_amount_of_slider":"スレイダーの変化量",
        
        # カーブ
        "flg_curve":"カーブの有無",
        "power_of_curve":"カーブの球威",
        "breaking_of_curve":"カーブのキレ",
        "control_of_curve":"カーブのコントロール",
        "change_amount_of_curve":"カーブの変化量",
        
        # フォーク
        "flg_fork":"フォークの有無",
        "power_of_fork":"フォークの球威",
        "breaking_of_fork":"フォークのキレ",
        "control_of_fork":"フォークのコントロール",
        "change_amount_of_fork":"フォークの変化量",
        
        # シンカー
        "flg_sinker":"シンカーの有無",
        "power_of_sinker":"シンカーの球威",
        "breaking_of_sinker":"シンカーのキレ",
        "control_of_sinker":"シンカーのコントロール",
        "change_amount_of_sinker":"シンカーの変化量",
        ### シュート ###
        "flg_shoot":"シュートの有無",
        "power_of_shoot":"シュートの球威",
        "breaking_of_shoot":"シュートのキレ",
        "control_of_shoot":"シュートのコントロール",
        "change_amount_of_shoot":"シュートの変化量",
        
        
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
        "pitcher_appropriate":"ピッチャー適正",
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
    widgets = {
      'career':forms.Select( 
        choices = [
          ('高卒', '高卒'),
          ('大卒', '大卒'),
          ('社会人', '社会人'),
          ('助っ人', '助っ人')
        ]
      )
    }
    
    # def __init__(self, *args, **kwargs):
    #     super(PlayerForm, self).__init__(*args, **kwargs)
    #     self.fields["main_position"].widget.attrs.update({
    #         "onchange": "update_appropriate_position();"
    #     })
