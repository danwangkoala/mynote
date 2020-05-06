from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note", null=True)
    tag = models.CharField(max_length=200)
    categroy = models.CharField(max_length=200)
    modify_date = models.DateTimeField("date modified")
    link = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.tag

