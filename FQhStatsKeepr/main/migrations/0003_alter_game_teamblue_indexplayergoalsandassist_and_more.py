# Generated by Django 4.0.4 on 2022-08-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_game_teamblue_players_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='teamBlue_indexPlayerGoalsandAssist',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='teamRed_indexPlayerGoalsandAssist',
            field=models.JSONField(),
        ),
    ]
