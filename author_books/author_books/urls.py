from django.contrib import admin
from django.urls import path, include
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list),
    path('library/<int:book_id>', views.book_detail, name='book_id')
]
