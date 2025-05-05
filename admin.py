from django.contrib import admin
from .models import products,cartmodel
# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=['name','category','trending','sale']

class cartadmin(admin.ModelAdmin):
    list_display=['name','category','trending','sale']


admin.site.register(products,productadmin)
admin.site.register(cartmodel,cartadmin)