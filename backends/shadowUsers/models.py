from django.db import models
from django.contrib import admin
from datetime import * 

# Create your models here.

class User(models.Model):
    type = models.CharField(max_length = 150)
    port = models.IntegerField()
    price = models.IntegerField()
    addDate = models.DateField()
    description = models.CharField(max_length = 150)

class UserAdmin(admin.ModelAdmin):
    def getUseDays(self, obj):
        delta =  date.today() - obj.addDate
        return delta.days
    getUseDays.short_description = u"useDays"
    list_display = ('type','port','price','addDate','getUseDays','description')

admin.site.register(User, UserAdmin)
