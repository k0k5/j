from django.db import models
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', help_text='Необязательное поле', max_length=100, blank=True)
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthday_images',blank=True)