from django.contrib import admin
from .models import *
# Register your models here.

class MainAdmin(admin.ModelAdmin):
    pass

admin.site.register(AccountLogin)
admin.site.register(AccountReigster)