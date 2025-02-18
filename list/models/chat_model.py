from django.db import models
from list.models import CustomUser


class Chat(models.Model):
    ROLE_CHOICES = [('user','user'),('system', 'system')]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    sender = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')
    text = models.TextField(null=True)