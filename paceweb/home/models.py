from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_id = models.CharField(max_length=200)
    user_point = models.IntegerField(default=0)
