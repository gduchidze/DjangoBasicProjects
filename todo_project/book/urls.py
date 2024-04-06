from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookView

router = DefaultRouter()
router.register(r'books', BookView)

urlpatterns = [
    path('', include(router.urls)),
]
