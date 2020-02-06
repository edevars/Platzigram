# Django
from django.contrib import admin

# Utils
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'user', 'profile')
    list_editable = ('photo',)
    search_fields = (
        'title',
        'description',
    )
