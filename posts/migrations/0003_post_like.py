# Generated by Django 4.0.1 on 2022-02-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(default=0, verbose_name='Like'),
        ),
    ]
