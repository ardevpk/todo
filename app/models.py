from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Testing(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.CharField(max_length=16, default='')
    Name = models.CharField(max_length=24, default='')
    Title = models.CharField(max_length=288, default='')
    Desc = HTMLField(max_length=512, default='')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class NewsApi(models.Model):
    News_id = models.AutoField(primary_key=True)
    News_image = models.CharField(max_length=1000, default='')
    News_title = models.CharField(max_length=1000, default='')
    News_author = models.CharField(max_length=100, default='')
    News_desc = HTMLField(max_length=10000000, default='')
    News_slug = AutoSlugField(populate_from='News_title', unique=True, default=None)


