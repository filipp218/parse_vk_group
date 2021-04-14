from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField("Текст поста",  max_length = 500, blank=False)
    date_of_post = models.DateField("Дата публикации", blank=False)
    id_from_vk = models.PositiveSmallIntegerField("ID сообщения из VK", blank=False)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return str(self.id_from_vk)

class PostImage(models.Model):
    post_id = models.PositiveSmallIntegerField("ID VK поста", blank=False)
    photo = models.ImageField("Картинка поста", blank=True)

    def __str__(self):
        return str(self.post_id)



