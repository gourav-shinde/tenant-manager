from django.contrib import admin
from django.urls import path,include
from .views import UserRecordView,registeration_view

app_name="accounts"
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('user/register',registeration_view, name='register'),
]

