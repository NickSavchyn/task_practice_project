from django.shortcuts import render
from django.views import generic, View

from TaskProject.forms import TaskForm, TagForm
from TaskProject.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "TaskProject/task_list.html"
    paginate_by = 5
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "TaskProject/task_form.html"
    success_url = "http://127.0.0.1:8000/task/create"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "TaskProject/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "TaskProject/tag_form.html"
    success_url = "http://127.0.0.1:8000/tags/create"

