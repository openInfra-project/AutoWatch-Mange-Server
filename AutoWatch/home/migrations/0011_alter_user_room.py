# Generated by Django 3.2.5 on 2021-08-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_user_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.IntegerField(default=0, verbose_name='Room 갯수'),
        ),
    ]