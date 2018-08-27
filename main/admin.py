from django.contrib import admin

# Register your models here.
from .models import Article, Reply, Like

admin.site.register(Article)
admin.site.register(Reply)
admin.site.register(Like)