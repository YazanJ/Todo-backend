from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    note_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_text
