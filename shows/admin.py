from django.contrib import admin

from shows.models import *

class ShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Show, ShowAdmin)