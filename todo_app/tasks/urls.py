from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('active/', views.task_list, name='task_list'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('history/', views.task_history, name='task_history'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('<int:pk>/uncomplete/', views.task_uncomplete, name='task_uncomplete'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/restore/', views.task_restore, name='task_restore'),
    path('<int:pk>/permanent-delete/', views.task_permanent_delete, name='task_permanent_delete'),
    path('bulk-action/', views.bulk_action, name='bulk_action'),
]