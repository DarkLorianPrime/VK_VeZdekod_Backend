import datetime
import os
import random
import time

import requests
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from memes_images.models import Meme, Author

url_template = "http://vk.darklorian.ru/photos/"


class GetAlbumPhoto(ViewSet):
    def like(self, request, *args, **kwargs):
        if request.data.get("id") is None:
            return Response({"error": "Please, insert <id> data."})
        meme = Meme.objects.filter(id=request.data.get("id"))
        if not meme.exists():
            return Response({"error": "Insert correct id."})
        likes = meme.first().likes_count
        meme.update(likes_count=likes + 1)
        return Response({"response": likes + 1})

    def dislike(self, request, *args, **kwargs):
        if request.data.get("id") is None:
            return Response({"error": "Please, insert <id> data."})
        meme = Meme.objects.filter(id=request.data.get("id"))
        if not meme.exists():
            return Response({"error": "Insert correct id."})
        likes = meme.first().likes_count
        if meme.first().likes_count > 0:
            meme.update(likes_count=likes - 1)
            likes -= 1
        return Response({"response": likes})

    def feed(self, request, *args, **kwargs):
        random.seed(datetime.datetime.now())
        rand_int = random.randint(0, 10)
        if rand_int in [1, 2]:
            return Response({"response": Meme.objects.filter().order_by("-priority")[:1].values()})
        if rand_int == 7:
            return Response({"response": Meme.objects.order_by('?').order_by("likes_count")[:1].values()})
        return Response({"response": Meme.objects.order_by('?')[:1].values()})

    def select_best(self, request, *args, **kwargs):
        if request.data.get("id") is None:
            return Response({"error": "Please, insert <id> data."})
        meme = Meme.objects.filter(priority=10)
        if meme.exists():
            meme.update(priority=0)
        meme = Meme.objects.filter(id=request.data["id"])
        meme.update(priority=10)
        return Response({"response": {"id": request.data["id"], "image": meme.first().file_name,
                                      "likes": meme.first().likes_count}})

    def get_best(self, request, *args, **kwargs):
        meme = Meme.objects.order_by("-priority").first()
        return Response({"response": {"image": meme.file_name, "likes": meme.likes_count}})

    def list(self, request, *args, **kwargs):
        all_memes = Meme.objects.all().values("id", 'user__name', 'user__surname', 'likes_count', 'file_name').order_by(
            "-likes_count")
        return Response({"response": all_memes})

    def create(self, request, *args, **kwargs):
        if request.data.get("owner") is None or request.data.get("album_id") is None:
            return Response({"error": "Get owner_id (without -) and album_id"})
        photos_list = requests.get("https://api.vk.com/method/photos.get",
                                   params={"owner_id": f"-{request.data['owner']}", "v": "5.130",
                                           "album_id": f"{request.data['album_id']}", "count": 1000,
                                           "access_token": os.getenv("access_token"), "extended": 1})
        items = photos_list.json()["response"]["items"]
        for id, item in enumerate(items):
            user = requests.get("https://api.vk.com/method/users.get",
                                params={"access_token": os.getenv("access_token"), "v": "5.130",
                                        "user_ids": [item["user_id"]]})
            print(user.json())
            user_info = user.json()["response"][0]
            author = Author.objects.get_or_create(name=user_info["first_name"], surname=user_info["last_name"])
            filename = f"{id}_{user_info['first_name']}"
            Meme.objects.get_or_create(user_id=author[0].id, likes_count=item["likes"]["count"],
                                       file_name=url_template + filename + ".png", priority=5)
            with open(f"photos/{filename}.png", "wb+") as file:
                file_content = requests.get(item["sizes"][-1]['url'])
                file.write(file_content.content)
            time.sleep(.5)
        return Response({"response": "ok"})
