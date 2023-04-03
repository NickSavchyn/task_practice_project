from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]


class Task(models.Model):
    content = models.CharField(max_length=63, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["created_at", "is_done"]

    def __str__(self):
        return f"Task: {self.content} ({self.tags})"

