from django.contrib import admin
from django.urls import path, include
from myapp.views import CustomAuthToken
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),
]

urlpatterns += doc_urls