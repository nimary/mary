from django.urls import path
from django.urls import URLPattern
from . import views


urlpatterns = [
    path('submit/expense/', views.submit_expense, name='submit_expense'),
    path('submit/income/', views.submit_income, name='submit_income'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/login/', views.login, name='logout'),
    path('', views.index, name='index'),
    
]