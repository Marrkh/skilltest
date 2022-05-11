from django.db import models


class TestTaken(models.Model):
    class Meta:
        verbose_name_plural = "Taken Tests"

    created_at = models.CharField(default='yesterday', max_length=250)
    public = models.BooleanField()
    result = models.IntegerField()
    canceled = models.BooleanField()
    test = models.ForeignKey('Test', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)

    @property
    def short_info(self):
        return f'{self.user} {self.created_at}'

    def __str__(self):
        return self.short_info