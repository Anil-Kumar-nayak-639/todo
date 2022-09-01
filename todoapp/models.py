from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class todolist(models.Model):
    manage = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    list=models.CharField(max_length=200)
    done=models.BooleanField(default=False)