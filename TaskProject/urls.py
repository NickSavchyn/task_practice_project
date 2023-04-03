from django.urls import path

from TaskProject.views import TaskListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    ]

app_name = "TaskProject"
