from django.contrib import admin
from .models import Type, Category, Pay_Method, Movement

# Register your models here.
admin.site.register(Movement)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Pay_Method)
