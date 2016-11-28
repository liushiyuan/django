from django.db import models
from django.contrib import admin

# Create your models here.

class EqshowPost(models.Model):
    enterprise = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)

class EqshowPostAdmin(admin.ModelAdmin):
    list_display = ('enterprise','name','phone')

admin.site.register(EqshowPost, EqshowPostAdmin)
