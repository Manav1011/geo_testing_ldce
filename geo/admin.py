from django.contrib import admin
from .models import geo_cordinates,allowed_classes

# Register your models here.

admin.site.register(geo_cordinates)
admin.site.register(allowed_classes)