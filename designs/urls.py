from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('registration.backends.default.urls')),
    re_path(r'^', include('users.urls', namespace="users"), name='users'),
    re_path(r'^', include('diagrams.urls', namespace="diagrams"), name='diagrams'),
]
