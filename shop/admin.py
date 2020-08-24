from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class ProductImageInline(admin.TabularInline):  # TabularInline StackedInline
    model = ProductImage
    fields = ['image', 'get_photo', 'is_active']
    readonly_fields = ['get_photo']
    extra = 0

    def get_photo(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='75' />")

    get_photo.short_description = 'Фото'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'des', 'category')
    # list_display_links =
    search_fields = ['name']
    list_editable = ['is_active', 'category']
    inlines = [ProductImageInline]


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75"')
        else:
            return "-"

    get_photo.short_description = 'Фото'




admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)