# tweet/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet" #db에 있는 table 이름이 tweet이다.

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
