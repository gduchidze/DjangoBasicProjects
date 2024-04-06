
from django.urls import path, include

urlpatterns = [
    path('api/todo/', include('todo.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/book/', include('book.urls')),
]
