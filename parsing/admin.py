from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


class PostImageInline(admin.TabularInline):
    model = models.PostImage
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="/media/{obj.photo}" width="300" height="300">')


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "date_of_post"
    list_display = ("vk_id", "text")
    search_fields = ["text"]
    list_filter = ["date_of_post"]
    inlines = [PostImageInline]


# Register your models here.


class PostImageAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="/media/{obj.photo}" width="300" height="300">')


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.PostImage, PostImageAdmin)
