from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    user_origin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    user_destination = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    pub_date = models.DateTimeField(default=timezone.now)
    text_message = models.CharField(max_length=250)

    #def __str__(self):
    #    return f"{self.user_origin.username} {self.user_destination.username} {self.pub_date}"