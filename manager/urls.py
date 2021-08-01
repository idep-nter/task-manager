from django.urls import path
from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('new_task/', views.NewTaskView.as_view(), name='new_task'),
    path('update_task/<int:pk>/', views.UpdateTaskView.as_view(),
         name='update_task'),
    path('<pk>/delete/', views.DeleteTaskView.as_view(), name='delete_task')
]