from django.contrib import admin

from .models import Images


class ImageAdmin(admin.ModelAdmin):
    list_display = ("image", "pub_date")


admin.site.register(Images, ImageAdmin)
