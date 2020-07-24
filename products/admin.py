from django.contrib import admin
from .models import Categories, Products

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'title',
        'slug',
        'description',
        'status'
    ]

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products)

