# Generated by Django 4.1.7 on 2023-03-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile',
            field=models.TextField(),
        ),
    ]
