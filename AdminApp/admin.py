from django.contrib import admin
from .models import Category,Cake
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cname']

class CakeAdmin(admin.ModelAdmin):
    list_display = ['id','cakename','price','description',
            'imageUrl','category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cake,CakeAdmin)