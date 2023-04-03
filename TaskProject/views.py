from django.shortcuts import render
from django.views import generic, View

from TaskProject.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "TaskProject/task_list.html"
    paginate_by = 5
    queryset = Task.objects.prefetch_related("tags")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "TaskProject/tag_list.html"
    paginate_by = 5


