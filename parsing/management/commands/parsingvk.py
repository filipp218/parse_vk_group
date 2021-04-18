from django.core.management.base import BaseCommand
import vk
import requests
import datetime
from django.utils.text import slugify
from parsing import models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--token", help="Введите токен из вк")
        parser.add_argument("--group_id", type=int, help="Введите id группы")

    def handle(self, *args, **options):
        post_in_database = set()
        query_id = models.Post.objects.all()
        for item in query_id:
            post_in_database.add(item.vk_id)
        token = f"{options['token']}"  # Сервисный ключ доступа
        session = vk.Session(access_token=token)  # Авторизация
        vk_api = vk.API(session)
        group_id = f"{options['group_id']}"
        wall_posts = vk_api.wall.get(owner_id=int(group_id) * -1, v=5.21)

        for row in wall_posts["items"]:
            if row["text"]:
                text = row["text"]
                id_vk = row["id"]
                date = datetime.datetime.fromtimestamp(row["date"])
                url = f"vk.com/public{group_id}?w=wall-{group_id}_{id_vk}"
                if id_vk in post_in_database:
                    post_from_database = models.Post.objects.get(vk_id=id_vk)
                    post_from_database.text = text
                else:
                    new_post = models.Post(
                        text=text, date_of_post=date, vk_id=id_vk, url=url
                    )
                    new_post.save()
                    if "attachments" in row:
                        for item in row["attachments"]:
                            if item["type"] == "photo":
                                img = item["photo"]
                                if "photo_1280" in img:
                                    url_img = img["photo_1280"]
                                elif "photo_807" in img:
                                    url_img = img["photo_807"]
                                elif "photo_604" in img:
                                    url_img = img["photo_604"]
                                elif "photo_130" in img:
                                    url_img = img["photo_130"]
                                elif "photo_75" in img:
                                    url_img = img["photo_75"]
                                try:
                                    p = requests.get(url_img)
                                    photo = p.content
                                except:
                                    photo = "can't_download"
                                if photo != "can't_download":
                                    slug = slugify(url_img)
                                    with open(f"media/{slug}.jpg", "wb") as out:
                                        out.write(p.content)
                                    add_photo = models.PostImage(
                                        post=new_post, photo=f"{slug}.jpg"
                                    )
                                    add_photo.save()
