from blog.models import Article
from blog.models import Category
from blog.models import Tag
from django.contrib import admin 

# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
