from django.contrib import admin
from .models import StockFunds, AmountAccount,Stock_form
# Register your models here.
admin.site.register(Stock_form)
admin.site.register(StockFunds)
admin.site.register(AmountAccount)
