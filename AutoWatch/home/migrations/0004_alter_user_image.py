# Generated by Django 3.2.5 on 2021-08-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='home', verbose_name='이미지'),
        ),
    ]