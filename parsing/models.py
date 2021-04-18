from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField("Текст поста", max_length=500, blank=False)
    date_of_post = models.DateField("Дата публикации", blank=False)
    vk_id = models.PositiveSmallIntegerField(
        "ID сообщения из VK", blank=False, unique=True
    )
    url = models.TextField(unique=True)

    def __str__(self):
        return str(self.vk_id)


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="Id поста",
        related_name="images",
        blank=False,
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("Картинка поста", blank=True)

    def __str__(self):
        return str(self.post)
