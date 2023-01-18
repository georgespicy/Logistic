from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
from autoslug import AutoSlugField


class User(AbstractUser):
    gender_choices = (
        ("male", "Male"),
        ("female", "Female"),
        ("custom", "custom"),        
    )
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_images",
        validators=[
            FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg", "webp"])
        ],
    )    
    bio = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True)
    phone_no = models.CharField(max_length=14, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=gender_choices, null=True, blank=True)    
    slug = AutoSlugField(unique=True, populate_from="username", sep="_", null=True)

    def initials(self):
        x = self.get_full_name()
        fullname = str(x)
        l = [] 
        for i in fullname.split(' '): 
            l.append(i[0]) 
        result = ".".join(l) + '.'
        return result
        
    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)