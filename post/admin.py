from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'uuid')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'title', 'category')
    list_filter = ('category__name',)

