from django.urls import path


from .views import index, TagListView, TaskListView, TaskCreateView, TagCreateView, TagUpdateView, TagDeleteView, \
    TaskDeleteView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name='index'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tags/create_tag/', TagCreateView.as_view(), name='tag_create'),
    path('tags/update/<int:pk>/', TagUpdateView.as_view(), name='tag_update'),
    path('tags/delete/<int:pk>/', TagDeleteView.as_view(), name='tag_delete'),
    path('create_task/', TaskCreateView.as_view(), name='task_create'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
]

app_name = 'todo_list'
