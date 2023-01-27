from django.contrib import admin
from .models import Contact, Incoterms, RequestQuote

# Register your models here.

@admin.register(RequestQuote)
class RequestQuoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Incoterms)
class IncotermsAdmin(admin.ModelAdmin):
    pass