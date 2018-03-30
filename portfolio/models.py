from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    # title size
    title = models.CharField('Title', max_length=100, unique=True)

    # unique article id
    unique_name = models.CharField('Unique ID', max_length=100, unique=True, primary_key=True)

    body = RichTextUploadingField('Content', null=True, blank=True, config_name='default')

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
        return self.name

