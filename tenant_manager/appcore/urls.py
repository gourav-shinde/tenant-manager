from django.contrib import admin
from django.urls import path,include

from appcore.views import (landing)

app_name="appcore"
urlpatterns = [
    path('',landing,name="landing")

]
