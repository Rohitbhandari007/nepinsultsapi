from statistics import mode
from django.db import models


class Insult(models.Model):
    detail = models.TextField()

    def __str__(self):
        return self.detail