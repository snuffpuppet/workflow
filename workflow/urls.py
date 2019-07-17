from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('action/<int:action_id>/', views.action, name='action'),
    path('activity/<int:activity_id>/', views.activity, name='activity'),
    path('activity/<int:activity_id>/task/<task_id>/', views.task, name='task'),
]