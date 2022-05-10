from email import message
from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ph_num = models.CharField(max_length=13)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    email = models.CharField(max_length=55)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        date = self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")
        return "Message from " + self.name + f" on {date}"
