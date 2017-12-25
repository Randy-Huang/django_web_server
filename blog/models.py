from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    # title size
    title = models.CharField('title', max_length=100)
    
    # body of content
    body = RichTextUploadingField(null=True, blank=True, config_name='default')

    # excerpt of content
    excerpt = models.CharField(max_length=200, blank=True)

    # classification by category (one to many)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)

    # classification by tag (many to many)
    tag = models.ManyToManyField(Tag, blank=True)

    # user's info of article from django.contrib.auth.models
    author = models.ForeignKey(User)
    
    # record to article crate and modify time
    created_time = models.DateTimeField(default=timezone.now)
    published_time = models.DateTimeField(blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def modify(self):
        self.modified_time = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    class Meta:
        pass


