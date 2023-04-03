from django import forms
from .models import players

# forms.pyの役割
## フォームの内容を表示
## フォームの内容が正しいかの確認。
## フォームの内容を処理。
class playerForm(forms.ModelForm):
  class Meta:
    model = players #テーブル名
    
    # カラム名
    fields = (
      "lastName",
      "firstName",
      "career",
      "age",
      "uniformNumber",
      "birthPlace",
      "handed",
      "bbox",
      "contact",
      "power",
      "speed",
      "steeling",
      "arm_strength",
      "arm_accuracy",
      "catch",
      "reaction",
      "profile",
      # "slug"
    )