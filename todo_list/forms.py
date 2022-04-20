from django import forms

from todo_list.models import Task


class TaskForm(forms.ModelForm):
        deadline = forms.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"], required=False)

        class Meta:
            model = Task
            fields = ['content', 'tags']