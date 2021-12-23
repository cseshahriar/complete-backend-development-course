from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'created_by')
    search_fields = ('title',)
    list_display_links = ('title',)