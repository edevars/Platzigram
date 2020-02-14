"""Users URLs"""
# Django
from django.urls import path

from users import views

urlpatterns = [

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='details'
    ),

    # Management
    path(route='login', view=views.login_view, name="login"),
    path(route='logout', view=views.logout_view, name="logout"),
    path(route='signup', view=views.sign_up_view, name="signup"),
    path(route='me/profile', view=views.update_profile, name='update')
]
