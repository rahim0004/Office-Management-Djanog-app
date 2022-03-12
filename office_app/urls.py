from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp/', views.all_emp, name='all_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('filter_emp/', views.filter_emp, name='filter_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp'),
    path('confirm/<int:id>/', views.confirm_emp, name='confirm_emp'),
    path('update/<int:id>/', views.update_emp, name='update_emp'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.loginStuff, name='user_login'),
    path('logout/', views.stuff_logout, name='logout'),
]
