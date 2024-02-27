from django.contrib import admin
from store.models import Category,Size,Product
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)