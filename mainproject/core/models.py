from statistics import mode
from django.db import models


class Insults(models.Model):
    insult = models.TextField()

    def __str__(self):
        return self.insult