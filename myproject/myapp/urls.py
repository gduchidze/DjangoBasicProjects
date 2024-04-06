from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    # path('', views.main_page),
    path('category/', category),
    path('student_id/<int:id>', student)
]

