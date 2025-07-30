from django.contrib import admin
from .models import Outer, Top, Bottom, Shoes

# Register your models here.

admin.site.register(Outer)
admin.site.register(Top)
admin.site.register(Bottom)
admin.site.register(Shoes)