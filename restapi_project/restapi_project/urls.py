from django.contrib import admin
from django.urls import path
from restapi_app.views import BookAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BookAPIView.as_view())
]
