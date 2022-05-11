from django.db import models


class Answer(models.Model):
    text = models.TextField(blank=True, null=True)
    is_correct = models.BooleanField(default=False, null=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.text
