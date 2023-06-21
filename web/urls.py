from django.urls import path
from django.urls import URLPattern
from . import views


urlpatterns = [
    path('submit/expense/', views.submit_expense, name='submit_expense')
]