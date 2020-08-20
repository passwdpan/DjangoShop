from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    id = models.AutoField(primary_key=True,unique=True,)
    username = models.CharField(max_length=32,unique=True,)

class Tag(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField表示自增字段； primary_key=True 表示是主键
    title = models.CharField(max_length=32)
    # state = models.BooleanField()
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.CharField(max_length=32)
    # def __str__(self):
    #     return self.title