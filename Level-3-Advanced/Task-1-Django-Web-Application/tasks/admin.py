"""Admin registration for the task manager app."""

from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """List tasks in the admin site with useful filters and search."""

    list_display = ("title", "owner", "completed", "created_at")
    list_filter = ("completed", "created_at")
    search_fields = ("title", "description", "owner__username")
