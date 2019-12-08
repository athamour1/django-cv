from django.contrib import admin
#from django.conf.urls import url
from django.urls import path

from .views import (
    index,
    job,
)


urlpatterns = [
    path('<int:job_id>', job),
    path('', index),
]
