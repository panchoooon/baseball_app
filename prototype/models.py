from django.db import models

#年齢など、入力値の最大最小値を見る。
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
# from autoslug import AutoSlugField
from django.urls import reverse

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

HANDED_CHOICES = [
  ("右投げ","右投げ"),
  ("左投げ", "左投げ")
]

BBOX_CHOICES = [
  ("右打ち","右打ち"),
  ("左打ち","左打ち"),
  ("両打ち","両打ち"),
]

# POSITION_CHOICES = [
#   ("P","P"),
#   ("CC","CC"),
#   ("1B","1B"),
#   ("2B","2B"),
#   ("3B","3B"),
#   ("SS","SS"),
#   ("LF","LF"),
#   ("CF","CF"),
#   ("RF","RF")
# ]


class players(models.Model):
  # id = models.IntegerField(primary_key=True, unique=True) #idにあたるキーは、djangoで自動生成されるので、記述しない。
  lastName = models.CharField(max_length=30)
  firstName = models.CharField(max_length=30)

  career = models.CharField(
    max_length=10,
    choices = CAREER_CHOICES
  )
  age = models.IntegerField(
    default=18,
    validators=[MinValueValidator(18),
                MaxValueValidator(55)]
  )
  uniformNumber = models.IntegerField(
    validators=[MinValueValidator(0),
                MaxValueValidator(199)]
  )
  birthPlace = models.CharField(
    max_length=10,
    default=0,
    choices = BIRTHPLACE_CHOICES
  )
  handed = models.CharField(
    max_length=5,
    choices = HANDED_CHOICES
  )
  bbox = models.CharField(
    max_length=5,
    choices=BBOX_CHOICES
  )
  # position = models.CharField(
  #   max_length=2,
  #   choices=POSITION_CHOICES
  # )
  contact = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  power = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  speed = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  steeling = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  arm_strength = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  arm_accuracy = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  catch = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  reaction = models.IntegerField(
    default=400,
    validators=[MinValueValidator(0),
                MaxValueValidator(1000)]
  )
  profile = models.TextField(
    default="がんばります！"
  )
  
  #スラグ
  slug = models.SlugField(blank=True)
  
  def __str__(self):
    return self.lastName + " " + self.firstName
  
  def get_absolute_url(self):
    return reverse("detail_player", kwargs={"slug": self.slug})