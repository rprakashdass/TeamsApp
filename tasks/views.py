from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Task

class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = "task"

    def get_queryset(self):
        return Task.objects.all