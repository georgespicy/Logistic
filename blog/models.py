from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from account.models import User
from django.core.validators import FileExtensionValidator
from django_quill.fields import QuillField
from django.urls import reverse

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
    
  
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Like")
        verbose_name_plural = ("Likes")

    def __str__(self):
      return f'{self.post} liked by {self.user}'
      
    def save(self, *args, **kwargs):
      self.slug = slugify(self.user)
      super().save(*args, **kwargs)
  

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Dislike")
        verbose_name_plural = ("Dislikes")

    def __str__(self):
      return f'{self.post} disliked by {self.user}'
      
    def save(self, *args, **kwargs):
      self.slug = slugify(self.user)
      super().save(*args, **kwargs)
      

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment = QuillField()
    date_commented = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f"{self.user}  ---  {self.post_comment}"

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})