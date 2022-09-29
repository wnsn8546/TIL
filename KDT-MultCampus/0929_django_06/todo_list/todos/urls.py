from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [ 
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('change-status/<int:todo_pk>', views.change_status, name='change_status'),
    path('update-form/<int:todo_pk>', views.update_form, name="update_form"),
    path('update/<int:todo_pk>', views.update, name='update'),
    path('delete/<int:todo_pk>', views.delete, name='delete'),
    ]