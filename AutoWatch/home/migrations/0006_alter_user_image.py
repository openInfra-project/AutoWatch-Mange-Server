# Generated by Django 3.2.5 on 2021-08-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null='/static/assets/images/face-recognition.png', upload_to='images/', verbose_name='이미지'),
        ),
    ]