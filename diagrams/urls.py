from django.urls import re_path

from . import views

app_name = "diagrams"

urlpatterns = [
    re_path(r'^projects/$', views.projects, name="projects"),
    re_path(r'^delete-project/(?P<pk>.*)/$', views.delete_project, name="delete_project"),
    re_path(r'^modules/(?P<pk>.*)/$', views.modules, name="modules"),
    re_path(r'^delete-module/(?P<pk>.*)/$', views.delete_module, name="delete_module"),
    re_path(r'^process/(?P<pk>.*)/$', views.process, name="process"),
    re_path(r'^delete-process/(?P<pk>.*)/$', views.delete_process, name="delete_process"),
]
