# Generated by Django 3.2.5 on 2021-08-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_user_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.IntegerField(default=0, max_length=200, verbose_name='Room 갯수'),
        ),
    ]