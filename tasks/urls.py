from django.urls import path
from . import views

urlpatterns = [
    path('tasksList/<int:pk>/', views.tasksList.as_view(),name='tasksList'),
    path('taskDetail/<int:pk>/', views.taskDetail.as_view(),name='taskDetail'),

]
