# from django import urls
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from blog_app.views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]