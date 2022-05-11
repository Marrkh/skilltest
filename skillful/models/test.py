from django.db import models
import datetime

DIFFICULTY_LEVELS = (
    ('1', 'easy'),
    ('2', 'medium'),
    ('3', 'hard'),
    ('4', 'expert'),
)


class Test(models.Model):
    title = models.CharField(
        verbose_name="Title",
        help_text="Title of the Test",
        max_length=250
    )
    description = models.TextField()
    time_interval = models.DurationField(default=datetime.timedelta(minutes=30))
    time_between_attempts = models.DurationField(default=datetime.timedelta(days=30))
    image = models.ImageField(upload_to='uploads/')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=False)
    difficulty_level = models.CharField(max_length=1, choices=DIFFICULTY_LEVELS, default='1')

    def __str__(self):
        return self.title
