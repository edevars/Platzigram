"""Platzigram URL module"""

from django.urls import path
from django.contrib import admin

from platzigram import local_views
from posts import posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('date-time/', local_views.see_date_time),
    path('sort/', local_views.sort_numbers),
    path('access/<str:name>/<int:age>', local_views.get_access_by_age),

    # Platzigram
    path('posts/', posts_views.list_posts)
]
