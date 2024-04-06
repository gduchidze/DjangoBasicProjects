from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('books/<str:title>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<str:title>/', views.edit_book),
    path('delete/<str:title>/', views.delete_book),
]


admin.site.site_header = "My Library"
admin.site.index_title = "My Library"