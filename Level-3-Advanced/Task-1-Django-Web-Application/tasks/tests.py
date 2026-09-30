"""Automated tests for the task manager app.

Run with:  python manage.py test
"""

from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from .models import Task


class AuthenticationTests(TestCase):
    """Registration, login and password reset."""

    def test_register_creates_and_logs_in_user(self):
        """POSTing the register form creates the user and logs them in."""
        response = self.client.post(
            reverse("register"),
            {
                "username": "newbie",
                "email": "newbie@example.com",
                "password1": "Str0ng-Passw0rd!",
                "password2": "Str0ng-Passw0rd!",
            },
        )
        self.assertRedirects(response, reverse("task-list"))
        self.assertTrue(User.objects.filter(username="newbie").exists())
        self.assertEqual(int(self.client.session["_auth_user_id"]),
                         User.objects.get(username="newbie").pk)

    def test_task_list_requires_login(self):
        """Anonymous visitors are redirected to the login page."""
        response = self.client.get(reverse("task-list"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('task-list')}")

    def test_password_reset_sends_email(self):
        """Password reset queues one email with a reset link."""
        User.objects.create_user("alice", "alice@example.com", "s3cret-pass")
        self.client.post(
            reverse("password_reset"), {"email": "alice@example.com"}
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("/accounts/reset/", mail.outbox[0].body)


class TaskTests(TestCase):
    """Task CRUD and per-user visibility."""

    def setUp(self):
        self.alice = User.objects.create_user("alice", password="pass-12345")
        self.bob = User.objects.create_user("bob", password="pass-12345")
        self.admin = User.objects.create_superuser("admin", password="adm-12345")
        self.alice_task = Task.objects.create(title="Alice task", owner=self.alice)

    def test_user_sees_only_own_tasks(self):
        """A regular user's list contains their tasks only."""
        self.client.force_login(self.alice)
        response = self.client.get(reverse("task-list"))
        tasks = response.context["tasks"]
        self.assertEqual(list(tasks), [self.alice_task])

    def test_admin_sees_all_tasks(self):
        """Staff users see everyone's tasks."""
        Task.objects.create(title="Bob task", owner=self.bob)
        self.client.force_login(self.admin)
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.context["tasks"].count(), 2)

    def test_create_task(self):
        """A logged-in user can create a task."""
        self.client.force_login(self.bob)
        self.client.post(reverse("task-create"), {"title": "Buy milk"})
        task = Task.objects.get(title="Buy milk")
        self.assertEqual(task.owner, self.bob)
        self.assertFalse(task.completed)

    def test_toggle_task_status(self):
        """POSTing toggle flips the completed flag."""
        self.client.force_login(self.alice)
        self.client.post(reverse("task-toggle", args=[self.alice_task.pk]))
        self.alice_task.refresh_from_db()
        self.assertTrue(self.alice_task.completed)

    def test_cannot_edit_other_users_task(self):
        """A regular user gets 404 when editing someone else's task."""
        self.client.force_login(self.bob)
        response = self.client.post(
            reverse("task-update", args=[self.alice_task.pk]), {"title": "hacked"}
        )
        self.assertEqual(response.status_code, 404)
        self.alice_task.refresh_from_db()
        self.assertEqual(self.alice_task.title, "Alice task")

    def test_delete_task(self):
        """The owner can delete their task."""
        self.client.force_login(self.alice)
        self.client.post(reverse("task-delete", args=[self.alice_task.pk]))
        self.assertFalse(Task.objects.filter(pk=self.alice_task.pk).exists())
