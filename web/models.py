from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default= uuid.uuid4, editable= False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name