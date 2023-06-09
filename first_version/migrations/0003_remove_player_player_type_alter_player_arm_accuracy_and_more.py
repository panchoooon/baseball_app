# Generated by Django 4.1.7 on 2023-05-07 05:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_version", "0002_alter_player_control_of_straight_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="player_type",
        ),
        migrations.AlterField(
            model_name="player",
            name="arm_accuracy",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="送球",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="arm_strength",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="肩力",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="catch",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="捕球精度",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="contact",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="ミート",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="control_of_straight",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="ストレートのコントロール",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="growth_of_straight",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="ストレートのノビ",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="main_position",
            field=models.CharField(
                choices=[
                    ("ピッチャー", "ピッチャー"),
                    ("キャッチャー", "キャッチャー"),
                    ("ファースト", "ファースト"),
                    ("セカンド", "セカンド"),
                    ("サード", "サード"),
                    ("ショート", "ショート"),
                    ("レフト", "レフト"),
                    ("センター", "センター"),
                    ("ライト", "ライト"),
                ],
                default="ピッチャー",
                max_length=12,
                verbose_name="メインポジション",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="mental_strength",
            field=models.PositiveSmallIntegerField(
                default=5,
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(5),
                ],
                verbose_name="メンタル",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="power",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="パワー",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="reaction",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="打球反応",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="speed",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="走力",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="stamina",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="スタミナ",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="sturdiness",
            field=models.PositiveSmallIntegerField(
                default=5,
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="ケガしにくさ",
            ),
        ),
        migrations.AlterField(
            model_name="player",
            name="vision",
            field=models.PositiveSmallIntegerField(
                default=200,
                validators=[
                    django.core.validators.MaxValueValidator(1000),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="選球眼",
            ),
        ),
    ]
