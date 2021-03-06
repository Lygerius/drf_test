from django.contrib import admin

from .models import Images


class ImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


admin.site.register(Images, ImageAdmin)
