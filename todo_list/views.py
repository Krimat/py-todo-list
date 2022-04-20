from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo_list.forms import TaskForm
from todo_list.models import Tag, Task


def index(request):
    return render(
        request=request,
        template_name='todo_list/index.html',
    )


class TagListView(ListView):
    model = Tag
    template_name = 'todo_list/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy('todo_list:tags')
    template_name = 'todo_list/tag_form.html'


class TagUpdateView(UpdateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy('todo_list:tags')
    template_name = 'todo_list/tag_form.html'


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('todo_list:tags')


class TaskListView(ListView):
    model = Task
    template_name = 'todo_list/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    form_class = TaskForm
    success_url = reverse_lazy('todo_list:index')
    template_name = 'todo_list/task_form.html'


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo_list:index')
    template_name = 'todo_list/task_form.html'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo_list:index')
    template_name = 'todo_list/task_delete_confirm.html'

