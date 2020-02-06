"""Platzigram URL module"""

from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from platzigram import local_views
from posts import posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_world,  name="hello_world"),
    path('date-time/', local_views.see_date_time, name="date"),
    path('sort/', local_views.sort_numbers, name="sort"),
    path('access/<str:name>/<int:age>',
         local_views.get_access_by_age, name="validate_age"),

    # Platzigram
    path('posts/', posts_views.list_posts, name="feed"),
    path('users/login', users_views.login_view, name="login"),
    path('users/logout', users_views.logout_view, name="logout"),
    path('users/signup', users_views.sign_up_view, name="signup")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
