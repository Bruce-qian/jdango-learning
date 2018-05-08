from django.contrib import admin
from . import models
# Register your models here.
class ArticleAdmiin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')

admin.site.register(models.Article, ArticleAdmiin)