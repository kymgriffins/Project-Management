from django.urls import path
from . import views 

urlpatterns = [
   path('', views.home, name='home'),
   path('projects/', views.project_list, name='projects'),
   path('project/<int:pk>/', views.project_details, name='project-details'),
   path('comments/', views.comment_list, name='comments'),
   path('comment/<int:pk>/', views.comment_details, name='comment-details'),
   path('dailyrecords/', views.dailyrecord_list, name='dailyrecords'),
   path('dailyrecord/<int:pk>/', views.dailyrecord_details, name='dailyrecord-details'),
   path('materials/', views.material_list, name='materials'),
   path('material/<int:pk>/', views.material_details, name='material-details'),
   path('material/used/', views.material_usage_list, name='material-usage'),
   path('material/used/<int:pk>/', views.material_usage_details, name='material-usage-details'),
   path('invoices/', views.invoice_list, name='invoice_list'),
   path('invoices/<int:pk>/', views.invoice_details, name='invoice_details'),
   path('blueprint/', views.create_blueprint, name='create_blueprint'),
    path('record_pic/', views.create_record_pic, name='create_record_pic'),
    path('building/', views.create_building, name='create_building'),
    path('projectsrecords/<int:pk>/', views.project_daily_records, name='project_daily_records'),
    path('invoice-items/', views.invoice_items),
    path('todos/', views.todo_list,  name='todo-list'),
    path('todos/<int:pk>/', views.todo_detail, name='todo-detail'), 
    path('structurals/', views.structurals_list, name='structurals-list'),
    path('structurals/<int:pk>/', views.structurals_details, name='structurals-details'),
    path('qs/', views.qs_list, name='qs-list'),
    path('qs/<int:pk>/', views.qs_details, name='qs-details'),
    path('architecturals/', views.architecturals_list, name='architecturals-list'),
    path('architecturals/<int:pk>/', views.architecturals_details, name='architecturals-details'),
    path('legals/', views.legals_list, name='legals-list'),
    path('legals/<int:pk>/', views.legals_details, name='legals-details'),
]

