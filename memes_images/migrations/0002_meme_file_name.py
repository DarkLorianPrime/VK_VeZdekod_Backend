# Generated by Django 4.0.4 on 2022-04-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes_images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='file_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
