# Generated by Django 4.1.7 on 2023-05-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_version", "0009_alter_player_good_cnt"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="image",
            field=models.ImageField(
                default="media/images/image001.png",
                upload_to="media/images/",
                verbose_name="見た目",
            ),
        ),
    ]
