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
    # enum of access Permission 
    ACCESS_PERMISSION = {
        0: u'manager',
        1: u'member',
        2: u'guest',
    }

    # title size
    title = models.CharField('Title', max_length=100, unique=True)

    # unique article id
    unique_name = models.CharField('Unique ID', max_length=100, unique=True, primary_key=True)

    # body of content
    body = RichTextUploadingField('Content', null=True, blank=True, config_name='default')

    # excerpt of content
    excerpt = models.CharField('Abstract', max_length=200, blank=True)

    # Access permission
    access = models.IntegerField('Access Permission', default=2, choices=ACCESS_PERMISSION.items())

    # classification by category (one to many)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, blank=True)

    # classification by tag (many to many)
    tag = models.ManyToManyField('Tag', blank=True)

    # Counter of likes 
    likes = models.PositiveIntegerField('Likes Counter', default=0)

    # Counter of views
    views = models.PositiveIntegerField('Views Counter', default=0)
    
    # record to article crate and modify time
    created_time = models.DateTimeField(default=timezone.now)
    published_time = models.DateTimeField(blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    def can_access(self, user):
        if self.access == 2:
            return True
        elif self.access == 1 and user.id: 
            return True 
        elif self.access == 0 and user.is_staff:
            return True 
            
        return False 
    
    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def modify(self):
        self.modified_time = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    class Meta: 
        ordering = ['-created_time']
