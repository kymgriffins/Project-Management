from django.urls import path

from . import views 



urlpatterns =[
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='projects'),
    path('project/<int:pk>/', views.project_details, name='project-details'),
    path('tasks/', views.task_list, name='tasks'),
    path('task/<int:pk>/', views.task_details, name='task-details'),
    path('teams/', views.team_list, name='teams'),
    path('team/<int:pk>/', views.team_details, name='team-details'),
    path('comments/', views.comment_list, name='comments'),
    path('comment/<int:pk>/', views.comment_details, name='comment-details'),
]