"""Views for the task manager app (register, list, create, update, delete)."""

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, TaskForm
from .models import Task


def _visible_tasks(user: User) -> QuerySet[Task]:
    """Tasks the user is allowed to see.

    Regular users see only their own tasks; staff (admin) users see all.
    """
    if user.is_staff:
        return Task.objects.all()
    return Task.objects.filter(owner=user)


def _can_modify(user: User, task: Task) -> bool:
    """True if the user may edit the task (owner, or admin)."""
    return user.is_staff or task.owner_id == user.id


def register(request: HttpRequest) -> HttpResponse:
    """Register a new user and log them in immediately."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account was created.")
            return redirect("task-list")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def task_list(request: HttpRequest) -> HttpResponse:
    """Show all tasks visible to the current user."""
    tasks = _visible_tasks(request.user)
    pending = tasks.filter(completed=False).count()
    done = tasks.filter(completed=True).count()

    context = {
        "tasks": tasks,
        "pending": pending,
        "done": done,
        "is_admin": request.user.is_staff,
    }
    return render(request, "tasks/task_list.html", context)


@login_required
def task_create(request: HttpRequest) -> HttpResponse:
    """Create a new task owned by the current user."""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, f"Task \"{task.title}\" created.")
            return redirect("task-list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form, "heading": "New Task"})


@login_required
def task_update(request: HttpRequest, pk: int) -> HttpResponse:
    """Edit a task's title, description and completion status."""
    task = get_object_or_404(_visible_tasks(request.user), pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f"Task \"{task.title}\" updated.")
            return redirect("task-list")
    else:
        form = TaskForm(instance=task)

    return render(
        request, "tasks/task_form.html", {"form": form, "heading": f"Edit: {task.title}"}
    )


@login_required
def task_toggle(request: HttpRequest, pk: int) -> HttpResponse:
    """Quickly flip a task's completed flag (POST only)."""
    if request.method != "POST":
        return redirect("task-list")

    task = get_object_or_404(_visible_tasks(request.user), pk=pk)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    state = "completed" if task.completed else "marked as pending"
    messages.success(request, f"Task \"{task.title}\" {state}.")
    return redirect("task-list")


@login_required
def task_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """Delete a task after confirmation."""
    task = get_object_or_404(_visible_tasks(request.user), pk=pk)

    if request.method == "POST":
        title = task.title
        task.delete()
        messages.success(request, f"Task \"{title}\" deleted.")
        return redirect("task-list")

    return render(request, "tasks/task_confirm_delete.html", {"task": task})
