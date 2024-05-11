from django.contrib import admin

from core.models import (
    Family,
    Person,
)

# Register your models here.
admin.site.register(Family)
admin.site.register(Person)
