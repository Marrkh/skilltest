from django.db import models
import datetime


class Subject(models.Model):
    title = models.CharField(
        verbose_name="Subject",
        max_length=250
    )
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title
