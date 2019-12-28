from django.contrib import admin
from .models import Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_published', 'price', 'list_date', 'account')
    list_display_links = ('id', 'title')
    list_filter = ('account', 'category',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'price')
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)