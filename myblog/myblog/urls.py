"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import blog_view
from portfolio.views import contact_view, projects_view, allgood_view
from inheritance.views import inheritance_view, contact_view, main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_view),
    # path('contacts/', contact_view),
    # path('projects/', projects_view),
    # path('allgood/', allgood_view, name="allgood"),
    path('inheritance/', inheritance_view),
    path('contact/', contact_view),
    path('', main_view, name="main_page"),
]
