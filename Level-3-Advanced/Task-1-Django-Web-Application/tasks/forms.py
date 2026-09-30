"""Forms for the task manager app."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task


class RegisterForm(UserCreationForm):
    """User registration form (username + optional email + password)."""

    email = forms.EmailField(required=False, help_text="Optional, used for password reset")

    class Meta:
        model = User
        fields = ("username", "email")


class TaskForm(forms.ModelForm):
    """Form for creating and editing a task."""

    class Meta:
        model = Task
        fields = ("title", "description", "completed")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "What needs to be done?"}),
            "description": forms.Textarea(
                attrs={"placeholder": "Optional details...", "rows": 4}
            ),
        }
