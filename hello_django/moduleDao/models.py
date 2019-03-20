from django.db import models
#创建ORM模型，通过对象关系映射可以不写sql就能实现数据库的CRUD#
# Create your models here.
from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    hobby = models.CharField(max_length=20)
    constellation = models.CharField(max_length=20)
