from django.urls import path
from django.urls import path
from . import views

urlpatterns=[
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="api-tasklist"),
    path('task-detail/<str:pk>/', views.taskList, name="api-tasklist"),
    path('task-create/', views.taskCreate, name="api-taskcreate"),
    path('task-update/<str:pk>/', views.taskUpdate, name="api-taskupdate"),
    path('task-delete/<str:pk>/', views.taskDelete, name="api-taskdelete"),
]