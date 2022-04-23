from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class Meme(models.Model):
    user = models.ForeignKey("Author", on_delete=models.CASCADE)
    likes_count = models.IntegerField()
    file_name = models.CharField(max_length=255)
    priority = models.IntegerField()
