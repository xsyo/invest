from django.contrib import admin

from .models import Package, Journal


admin.site.register(Package)
admin.site.register(Journal)
