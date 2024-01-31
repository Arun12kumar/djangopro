from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('table/', views.table, name='table'),
    path('detailed/<str:pk>', views.detailed, name='detailed'),
    path('delete/<str:pk>',views.deleted, name="deleted"),
    path('edit/<str:pk>',views.edited, name="edited"),
    path('home/', views.home, name='home'),
    path('user/', views.userlog, name='userlog'),
    path('newlogin/', views.newlogin, name='newlogin'),
    path('alog/', views.alog, name='alog'),
]