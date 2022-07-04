from django.contrib import admin

from backend.models import BookTable, FoodItem

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(BookTable)
