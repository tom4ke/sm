from django.contrib import admin
from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'moderator')
    list_display_links = ('id', 'title')
    list_filter = ('moderator',)
    search_fields = ('title', 'moderator')
    list_per_page = 30
admin.site.register(Category, CategoryAdmin)