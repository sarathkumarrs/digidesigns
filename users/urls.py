from django.urls import re_path

from . import views

app_name = 'users'

urlpatterns = [
    re_path(r'^sign-up/$', views.sign_up, name='sign_up'),
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^profile/$', views.profile, name='profile'),
]
