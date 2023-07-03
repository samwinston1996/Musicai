from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "display_image", "creator", "visible", "date_created"]
    list_display_links = ["id", "display_image", "creator", "visible", "date_created"]
    list_per_page = 50

    def display_image(self, obj):
        return mark_safe(f"<img src='/media/{obj.image}' width='50' height='50' />")

    display_image.short_description = "Generated Image"

    def creator(self, obj):
        return obj.user.email


admin.site.register(Gallery, GalleryAdmin)