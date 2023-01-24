from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from account.models import User
from django.core.validators import FileExtensionValidator
from django_quill.fields import QuillField


class Category(models.Model):
  name = models.CharField(max_length=150)
  slug = AutoSlugField(unique=True, populate_from='name', sep='-', null=True)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super().save(*args, **kwargs)
  
  class Meta:
    verbose_name_plural = "Categories"


"""
todo Post Fields
*comments
*likes
"""


class Post(models.Model):
  title = models.CharField(max_length=255) 
  author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Author")
  short_description = models.TextField(null=True, blank=True)
  post_image = models.ImageField(      
    upload_to='posts/images',
    validators=[
        FileExtensionValidator(
          allowed_extensions=[
              'png', 'jpg', 'jpeg', 'webp'
          ]
        )
    ]
  )
  post_content = QuillField()
  categories = models.ManyToManyField(Category, related_name='categories')
  slug = AutoSlugField(unique=True, populate_from='title', sep='-', null=True)
  last_updated = models.DateField(auto_now=True)
  date_posted = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.title}'
      
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)