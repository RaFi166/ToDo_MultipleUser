from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings 
from task import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login',views.login, name="login"),
    path('logout',views.logout, name = 'logout'),
    path('task_save', views.task_save, name='task_save'),
    path('delete_task/<int:id>', views.delete_task),
    path('change_status/<int:id>/<str:status>', views.change_task),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
