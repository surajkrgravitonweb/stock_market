from django.contrib import admin
from .models import AccountLogin
# Register your models here.

class MainAdmin(admin.ModelAdmin):
    pass

admin.site.register(AccountLogin)