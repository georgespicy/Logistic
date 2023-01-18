from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(unique=True, populate_from='name', sep='-', null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.name

    def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)