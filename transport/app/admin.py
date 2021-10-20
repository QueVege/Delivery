from django.contrib import admin
from .models import (
    Company, Category, Driver, Transport
)

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Driver)
admin.site.register(Transport)

