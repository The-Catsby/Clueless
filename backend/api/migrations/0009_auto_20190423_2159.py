# Generated by Django 2.1.7 on 2019-04-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_player_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestate',
            name='whose_turn',
            field=models.OneToOneField(on_delete=False, to='api.Player'),
        ),
    ]
