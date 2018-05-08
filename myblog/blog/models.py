from django.db import models

# Create your models here
class Article(models.Model):
    title = models.CharField(max_length=32, default='TITLE')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True) #创建对象时自动加上当前时间

    def __str__(self):
        return self.title