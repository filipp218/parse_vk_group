import vk
import requests

token = "dacf0986dacf0986dacf0986f8dab8697dddacfdacf0986babad6c64a42075dcd6baba9"  # Сервисный ключ доступа
session = vk.Session(access_token=token)  # Авторизация
vk_api = vk.API(session)
wall_posts = vk_api.wall.get(owner_id=-178050421, v=5.21)
group_id = '178050421'
for row in wall_posts['items']:
    if 'text' in row:
        text = row['text']
        id_vk = row['id']
        data = row['date']
        url = f'vk.com/public{group_id}?w=wall-{group_id}_{id_vk}'
        for image in row['attachments']:
            if image["type"] == "photo":
                img = image["photo"]
                url_img = img["photo_1280"]
                try:
                    p = requests.get(url_img)
                photo = p.content


