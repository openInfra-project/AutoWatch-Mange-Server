# Generated by Django 3.2.5 on 2021-08-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210813_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='list',
            field=models.IntegerField(default=0, verbose_name='list 변수'),
        ),
    ]
