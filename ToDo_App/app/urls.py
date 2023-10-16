from django.urls import path
from . import views

urlpatterns = [
     # Home Page url
    path('',views.index, name='Home'), 
    
    # Register url
    path('register/',views.register, name='register'),

    # Login url
    path('login/',views.login, name='login'),

    # Logout url
    path('logout/',views.logout, name='logout'),

    # Create task url
    path('createTask/',views.createTask, name='creatTask'),

    # Completed task url
    path('completed/<int:pk>',views.completed, name='completed'),

    # incompleted task url
    path('inComplete/<int:pk>',views.inComplete, name='inComplete'),

    # Update task url
    path('update/<int:id>',views.updateTask,name='updateTask'),

    # Delete task url
    path('delete/<int:id>',views.deleteTask,name='deleteTask'),

]