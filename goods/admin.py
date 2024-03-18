from django.contrib import admin
from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'display_id')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('display_id',)
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'is_visible', 'description', 'category', 'price', 'discount', 'quantity')
        }),
        ('Изображения', {
            'fields': ('image', 'image2', 'image3', 'image4', 'image5')
        }),
    )