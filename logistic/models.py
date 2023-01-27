from django.db import models

# Create your models here.

class RequestQuote(models.Model):
    catagories  = [
        ('catagories', 'Catagories One'),
        ('catagories', 'Catagories Two'),
        ('catagories', 'Catagories Three'),
        ('catagories', 'Catagories Four'),
    ]
    extra_service = [
        ('freight', 'Freight'),
        ('express Delivery', 'Express Delivery'),
        ('insurance', 'Insurance'),
        ('packaging', 'Packaging')
    ]
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
    freight_type = models.CharField(max_length=20, blank=True, null=True, choices=catagories, default=None)
    incoterms = models.CharField(max_length=50, blank=True, null=True)
    city_of_department = models.CharField(max_length=100, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    lenght = models.IntegerField(blank=True, null=True)
    extra_service = models.CharField(choices=extra_service, default='freight', max_length=20, null=True)

class Incoterms(models.Model):
    incoterms = models.CharField(max_length=50, blank=True, null=True)

class Contact(models.Model):
    message = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)