from django.db import models


class Question(models.Model):
    code = models.TextField(blank=True, null=True)
    is_multiple_choice = models.BooleanField()
    type = models.CharField(max_length=250)
    test = models.ForeignKey('Test', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.code

