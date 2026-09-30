"""URL configuration for the config project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Task manager app (register, list, create, update, delete)
    path('', include('tasks.urls')),
    # Django's built-in auth views: login, logout, password reset
    path('accounts/', include('django.contrib.auth.urls')),
]
