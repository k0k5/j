from django.db import models


class Birthday(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    birthday = models.DateField()
    # добавьте нужные вам поля