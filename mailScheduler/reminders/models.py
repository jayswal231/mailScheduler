from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField()
    schedule_time = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject