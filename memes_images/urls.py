from django.urls import path

from memes_images.views import GetAlbumPhoto

urlpatterns = [
    path("getphotos/", GetAlbumPhoto.as_view({"get": "list", "post": "create"})),
    path("photos/best", GetAlbumPhoto.as_view({"get": "get_best", "post": "select_best"})),
    path("feed/", GetAlbumPhoto.as_view({"get": "feed"})),
    path("like/", GetAlbumPhoto.as_view({"post": "like"})),
    path("dislike/", GetAlbumPhoto.as_view({"post": "dislike"}))
]