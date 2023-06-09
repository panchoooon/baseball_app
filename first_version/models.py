from django.db import models

# Create your models here.
from django.conf import settings

from django.core.validators import MaxValueValidator, MinValueValidator #最大最小を設定

from django.contrib.auth.models import User #ユーザー



CAREER_CHOICES = [
  ('高卒', '高卒'),
  ('大卒', '大卒'),
  ('社会人', '社会人'),
  ('助っ人', '助っ人')
]

BIRTHPLACE_CHOICES = [
  ("北海道","北海道"),
  ("青森県","青森県"),
  ("岩手県","岩手県"),
  ("宮城県","宮城県"),
  ("秋田県","秋田県"),
  ("山形県","山形県"),
  ("福島県","福島県"),
  ("茨城県","茨城県"),
  ("栃木県","栃木県"),
  ("群馬県","群馬県"),
  ("埼玉県","埼玉県"),
  ("千葉県","千葉県"),
  ("東京都","東京都"),
  ("神奈川県","神奈川県"),
  ("新潟県","新潟県"),
  ("富山県","富山県"),
  ("石川県","石川県"),
  ("福井県","福井県"),
  ("山梨県","山梨県"),
  ("長野県","長野県"),
  ("岐阜県","岐阜県"),
  ("静岡県","静岡県"),
  ("愛知県","愛知県"),
  ("三重県","三重県"),
  ("滋賀県","滋賀県"),
  ("京都府","京都府"),
  ("大阪府","大阪府"),
  ("兵庫県","兵庫県"),
  ("奈良県","奈良県"),
  ("和歌山県","和歌山県"),
  ("鳥取県","鳥取県"),
  ("島根県","島根県"),
  ("岡山県","岡山県"),
  ("広島県","広島県"),
  ("山口県","山口県"),
  ("徳島県","徳島県"),
  ("香川県","香川県"),
  ("愛媛県","愛媛県"),
  ("高知県","高知県"),
  ("福岡県","福岡県"),
  ("佐賀県","佐賀県"),
  ("長崎県","長崎県"),
  ("熊本県","熊本県"),
  ("大分県","大分県"),
  ("宮崎県","宮崎県"),
  ("鹿児島県","鹿児島県"),
  ("沖縄県","沖縄県"),
  ("台湾","台湾"),
  ("キューバ","キューバ"),
  ("イタリア","イタリア"),
  ("パナマ","パナマ"),
  ("韓国","韓国"),
  ("オーストラリア","オーストラリア"),
  ("中国","中国"),
  ("チェコ共和国","チェコ共和国"),
  ("アメリカ","アメリカ"),
  ("メキシコ","メキシコ"),
  ("コロンビア","コロンビア"),
  ("カナダ","カナダ"),
  ("イギリス","イギリス"),
  ("プエルトリコ","プエルトリコ"),
  ("ドミニカ共和国","ドミニカ共和国"),
  ("イスラエル","イスラエル"),
  ("ニカラグア","ニカラグア")
]

THROW_CHOICES = [
  ("右","右"),
  ("左","左")
]

BBOX_CHOICES = [
  ("右","右"),
  ("左","左"),
  ("両","両")
]

PLAYER_TYPE_CHOICES = [
  ("投手","投手"),
  ("野手","野手"),
  ("二刀流","二刀流")
]

CHARACTER_CHOICES = [
  ("ふつう","ふつう"),
  ("内気","内気"),
  ("熱血","熱血"),
  ("お調子者","お調子者"),
  ("しっかり者","しっかり者"),
  ("クール","クール"),
  ("天然","天然"),
  ("したたか","したたか"),
  ("職人肌","職人肌"),
]

PITHING_FORM_CHOICES = [
  ("オーバースロー","オーバースロー"),
  ("スリークォーター","スリークォーター"),
  ("サイドスロー","サイドスロー"),
  ("アンダースロー","アンダースロー"),
]

MAIN_POSITION_CHOICES = [
  ("pitcher", "ピッチャー"),
  ("catcher","キャッチャー"),
  ("first", "ファースト"),
  ("second", "セカンド"),
  ("third", "サード"),
  ("shortstop", "ショート"),
  ("left", "レフト"),
  ("center", "センター"),
  ("right", "ライト")
]

POSITION_APPROPRIATE_CHOICES =[
  ("◎", "◎"),
  ("〇", "〇"),
  ("△", "△"),
  ("×", "×"),
]

class Player(models.Model):
  
  # 主キー (プレイヤーID)
  # id = models.AutoField(primary_key=True)
  player_id = models.AutoField(primary_key=True)

  # 作成者(ログインユーザー)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

  ##################
  # 選手プロフィール #
  ##################
  lastName = models.CharField("姓", max_length=10)
  firstName = models.CharField("名", max_length=10)
  career = models.CharField(
    "経歴",
    default="高卒",
    max_length=12,
    choices=CAREER_CHOICES
  )
  
  #"入団時の"年齢
  age = models.PositiveSmallIntegerField(
    "入団時の年齢",
    default=18,
    validators =[MaxValueValidator(40), MinValueValidator(18)]
  )
  
  # プロ年数
  number_of_years = models.PositiveSmallIntegerField(
    "プロ年数",
    default=1,
    validators =[MinValueValidator(1)]
  )
  height = models.PositiveSmallIntegerField(
    "身長",
    default=180,
    validators =[MaxValueValidator(220), MinValueValidator(150)]
  )
  weight = models.PositiveSmallIntegerField(
    "体重",
    default=80,
    validators =[MaxValueValidator(130), MinValueValidator(50)]
  )
  uniformNumber = models.SmallIntegerField(
    "背番号",
    default=1,
    validators =[MaxValueValidator(999), MinValueValidator(0)]
  )
  birthPlace = models.CharField(
    "出身地",
    max_length=10,
    default="東京都",
    choices = BIRTHPLACE_CHOICES
  )
  throw = models.CharField(
    "利き腕",
    max_length=5,
    default="右",
    choices = BBOX_CHOICES
  )
  bbox = models.CharField(
    "打席",
    max_length=5,
    default="右",
    choices = BBOX_CHOICES
  )
  # 選手タイプが投手の場合、選択不可
  main_position = models.CharField(
    "メインポジション",
    default=MAIN_POSITION_CHOICES[0][0],
    max_length=12,
    choices=MAIN_POSITION_CHOICES
  )
  
  character = models.CharField(
    "キャラクター",
    max_length = 10,
    default = "ふつう",
    choices = CHARACTER_CHOICES
  )
  
  image = models.ImageField(
    "見た目",
    upload_to="media/images/",
    default="media/images/image001.png"
  )
  profile = models.TextField(
    "プロフィール", 
    max_length=150,
    default = "がんばります！！"
  )
  
  # 守備適正
  pitcher_appropriate = models.CharField(
    "ピッチャー適正",
    default=POSITION_APPROPRIATE_CHOICES[0][0], #メインポジションの初期値がピッチャーなので、デフォルトの適正を◎とする。
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  catcher_appropriate = models.CharField(
    "キャッチャー適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  
  first_appropriate = models.CharField(
    "ファースト適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
    
  second_appropriate = models.CharField(
    "セカンド適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  third_appropriate = models.CharField(
    "サード適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  shortstop_appropriate = models.CharField(
    "ショート適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  left_appropriate = models.CharField(
    "レフト適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  center_appropriate = models.CharField(
    "センター適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  right_appropriate = models.CharField(
    "ライト適正",
    default=POSITION_APPROPRIATE_CHOICES[3][0],
    max_length=10,
    choices=POSITION_APPROPRIATE_CHOICES
  )
  # 守備適正
  
  
  ###########
  # 投手能力 #
  ###########
  pitching_form = models.CharField(
    "投球フォーム",
    max_length=20,
    default=PITHING_FORM_CHOICES[0][0], #オーバースロー
    choices=PITHING_FORM_CHOICES
  )
  stamina = models.PositiveSmallIntegerField(
    "スタミナ",
    default=500,
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  maximum_ball_speed = models.PositiveSmallIntegerField(
    "最大球速",
    default=100,
    validators =[MaxValueValidator(175), MinValueValidator(100)]
  )
  power_of_straight = models.PositiveSmallIntegerField(
    "ストレートの球威",
    default=500,
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  growth_of_straight = models.PositiveSmallIntegerField(
    "ストレートのノビ",
    default=500,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  control_of_straight = models.PositiveSmallIntegerField(
    "ストレートのコントロール",
    default=500,
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  mental_strength = models.PositiveSmallIntegerField(
    "メンタル",
    default=5,
    validators =[MaxValueValidator(10), MinValueValidator(5)]
  )
  strike_out = models.PositiveSmallIntegerField(
    "奪三振",
    default=5,
    validators =[MaxValueValidator(10), MinValueValidator(5)]
  )
  ##ここから変化球##
  
  ### スライダー ###
  flg_slider = models.BooleanField(
    "スライダーの有無",
    default = False,
  )
  power_of_slider = models.PositiveSmallIntegerField(
    "スライダーの球威",
    default = 1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  breaking_of_slider = models.PositiveSmallIntegerField(
    "スライダーのキレ",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  control_of_slider = models.PositiveSmallIntegerField(
    "スライダーのコントロール",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  change_amount_of_slider = models.PositiveSmallIntegerField(
    "スレイダーの変化量",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  ### カーブ ###
  flg_curve = models.BooleanField(
    "カーブの有無",
    default = False,
  )
  power_of_curve = models.PositiveSmallIntegerField(
    "カーブの球威",
    default = 1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  breaking_of_curve = models.PositiveSmallIntegerField(
    "カーブのキレ",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  control_of_curve = models.PositiveSmallIntegerField(
    "カーブのコントロール",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  change_amount_of_curve = models.PositiveSmallIntegerField(
    "カーブの変化量",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  ### フォーク ###
  flg_fork = models.BooleanField(
    "フォークの有無",
    default = False,
  )
  power_of_fork = models.PositiveSmallIntegerField(
    "フォークの球威",
    default = 1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  breaking_of_fork = models.PositiveSmallIntegerField(
    "フォークのキレ",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  control_of_fork = models.PositiveSmallIntegerField(
    "フォークのコントロール",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  change_amount_of_fork = models.PositiveSmallIntegerField(
    "フォークの変化量",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  ### シンカー ###
  flg_sinker = models.BooleanField(
    "シンカーの有無",
    default = False,
  )
  power_of_sinker = models.PositiveSmallIntegerField(
    "シンカーの球威",
    default = 1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  breaking_of_sinker = models.PositiveSmallIntegerField(
    "シンカーのキレ",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  control_of_sinker = models.PositiveSmallIntegerField(
    "シンカーのコントロール",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  change_amount_of_sinker = models.PositiveSmallIntegerField(
    "シンカーの変化量",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  ### シュート ###
  flg_shoot = models.BooleanField(
    "シュートの有無",
    default = False,
  )
  power_of_shoot = models.PositiveSmallIntegerField(
    "シュートの球威",
    default = 1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  breaking_of_shoot = models.PositiveSmallIntegerField(
    "シュートのキレ",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  control_of_shoot = models.PositiveSmallIntegerField(
    "シュートのコントロール",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  change_amount_of_shoot = models.PositiveSmallIntegerField(
    "シュートの変化量",
    default=1,
    help_text="1~1000",
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )


  ###########
  # 野手能力 #
  ###########
  contact = models.PositiveSmallIntegerField(
    "ミート",
    default=500,
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  power = models.PositiveSmallIntegerField(
    "パワー",
    default=500,
    validators =[MaxValueValidator(1000), MinValueValidator(1)]
  )
  vision = models.PositiveSmallIntegerField(
    "選球眼",
    default=500,
    validators = [MaxValueValidator(1000), MinValueValidator(1)]
  )
  speed = models.PositiveSmallIntegerField(
    "走力",
    default=500,
    validators = [MaxValueValidator(1000), MinValueValidator(1)]
  )
  arm_strength = models.PositiveSmallIntegerField(
    "肩力",
    default=500,
    validators = [MaxValueValidator(1000), MinValueValidator(1)]
  )
  arm_accuracy = models.PositiveSmallIntegerField(
    "送球",
    default=500,
    validators = [MaxValueValidator(1000), MinValueValidator(1)]
  )
  reaction = models.PositiveSmallIntegerField(
    "打球反応",
    default=500,
    validators = [MaxValueValidator(1000), MinValueValidator(1)]
  )
  catch = models.PositiveSmallIntegerField(
    "捕球精度",
    default=500,
    validators = [MaxValueValidator(1000), MinValueValidator(1)]
  )
  

  chance = models.PositiveSmallIntegerField(
    "チャンス",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  vs_left_pitcher = models.PositiveSmallIntegerField(
    "対左投手",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  inside = models.PositiveSmallIntegerField(
    "インコース",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  outside = models.PositiveSmallIntegerField(
    "アウトコース",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  high_ball = models.PositiveSmallIntegerField(
    "ハイボール",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  low_ball = models.PositiveSmallIntegerField(
    "ローボール",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  bunt = models.PositiveSmallIntegerField(
    "バント",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  base_running = models.PositiveSmallIntegerField(
    "走塁",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  steeling = models.PositiveSmallIntegerField(
    "盗塁",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  pitcher_lead = models.PositiveSmallIntegerField(
    "投手リード",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  home_block = models.PositiveSmallIntegerField(
    "ブロック",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  sturdiness = models.PositiveSmallIntegerField(
    "ケガしにくさ",
    default=5,
    validators = [MaxValueValidator(10), MinValueValidator(1)]
  )
  good_cnt = models.BigIntegerField(
    "いいね",
    default=0,
    validators = [MinValueValidator(0)]
    
  )

  def __str__(self):
    return self.lastName