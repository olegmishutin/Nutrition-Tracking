from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.indexView, name='index'),
    path('reg/', views.registerView, name='reg'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
