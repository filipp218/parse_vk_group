from . import models
import vk
import requests


post_in_database = {}
query_id = models.Post.objects.all()[3]
for item in query_id:
    post_in_database.add(item.id)

token = "dacf0986dacf0986dacf0986f8dab8697dddacfdacf0986babad6c64a42075dcd6baba9"  # Сервисный ключ доступа
session = vk.Session(access_token=token)  # Авторизация
vk_api = vk.API(session)
wall_posts = vk_api.wall.get(owner_id=-178050421, v=5.21)
group_id = '178050421'

for row in wall_posts['items']:
    if 'text' in row:
        text = row['text']
        id_vk = row['id']
        date = row['date']
        url = f'vk.com/public{group_id}?w=wall-{group_id}_{id_vk}'
        if id_vk in post_in_database:
            pass
        else:
            new_post = models.Post(text=text, date_of_post=date, id_from_vk=id_vk, url=url)
            new_post.save()

        for item in row['attachments']:
            photo = ""
            if item["type"] == "photo":
                img = item["photo"]
                url_img = img["photo_1280"]
                try:
                    p = requests.get(url_img)
                    photo = p.content
                except:
                    photo = "can't_download"
            if photo != "can't_download":
                add_photo = models.PostImage(post_id=id_vk, photo=photo)
                add_photo.save()





