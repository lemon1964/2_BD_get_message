from django.db import models
# from django.conf import settings
from django.utils import timezone
# from ckeditor_uploader.fields import RichTextUploadingField
# from taggit.managers import TaggableManager
# from django.contrib.auth.models import User


# Create your models here.


class MessageFront(models.Model):
    user = models.CharField(max_length=30)
    date = models.DateField(default=timezone.now)
    screen = models.CharField(max_length=20)
    event = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user} - {self.date} - {self.screen} - {self.event}'


