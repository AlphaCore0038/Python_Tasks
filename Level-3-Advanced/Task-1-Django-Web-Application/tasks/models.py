"""Models for the task manager app."""

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """A single to-do task owned by a registered user."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Optional details")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    class Meta:
        ordering = ["-created_at"]  # newest first

    def __str__(self) -> str:
        """Human-readable representation used in the admin site."""
        return self.title
