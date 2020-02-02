"""Platzigram URL module"""

from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('date-time/', views.see_date_time),
    path('sort/', views.sort_numbers),
    path('access/<str:name>/<int:age>', views.get_access_by_age),
]
