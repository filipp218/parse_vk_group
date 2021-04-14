from . import models
import vk
import requests
import datetime


def sluggen(text):
    """функция, которая генерирует slug
    для добавленных изображений исходя
    из их имени или ссылке откуда они скачаны"""
    slug = ''
    alphabet = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm','1','2','3','4','5','6','7','8','9','0'}
    russian = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
                'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
                'я': 'ya', ' ': '-'}
    for i in str(text):
        if i in alphabet:
            slug += str(i)
        elif i in russian:
            slug += str(russian[i])
    return slug


def down():
    post_in_database = {}
    query_id = models.Post.objects.all()
    for item in query_id:
        post_in_database.add(item.id_vk)
        print(item)

    token = "dacf0986dacf0986dacf0986f8dab8697dddacfdacf0986babad6c64a42075dcd6baba9"  # Сервисный ключ доступа
    session = vk.Session(access_token=token)  # Авторизация
    vk_api = vk.API(session)
    wall_posts = vk_api.wall.get(owner_id=-178050421, v=5.21)
    group_id = '178050421'

    for row in wall_posts['items']:
        print(row)
        if 'text' in row:
            text = row['text']
            id_vk = row['id']
            date = datetime.datetime.fromtimestamp(row['date'])
            url = f'vk.com/public{group_id}?w=wall-{group_id}_{id_vk}'
            if id_vk in post_in_database:
                pass
            else:
                new_post = models.Post(text=text, date_of_post=date, id_from_vk=id_vk, url=url)
                new_post.save()
            if 'attachments' in row:
                for item in row['attachments']:
                    p = None
                    if item["type"] == "photo":
                        img = item["photo"]
                        url_img = img["photo_1280"]
                        try:
                            p = requests.get(url_img)
                            photo = p.content
                        except:
                            photo = "can't_download"
                        if photo != "can't_download":
                            slug = sluggen(url_img)
                            with open(f'media/{slug}.jpg', "wb") as out:
                                out.write(p.content)
                            add_photo = models.PostImage(post_id=id_vk, photo=f'{slug}.jpg')
                            add_photo.save()





