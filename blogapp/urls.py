from django.urls import path
from .views import Result, datenew

urlpatterns = [
    path('',datenew, name='datenew'),
    path('result/',Result.as_view(), name='result')
]
