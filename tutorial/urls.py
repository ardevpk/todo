"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from tutorial.views import test15

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name='test'),
    # path('test/', views.test, name='test'),
    # path('test2/', views.test2, name='test2'),
    # path('test3/<int:id>/', views.test3, name='test3'),
    # path('test4/<str:id>/', views.test4, name='test4'),
    # path('test5/<slug:id>/', views.test5, name='test5'),
    # path('test6/<id>/', views.test6, name='test6'),
    # path('<id>/', views.test7, name='test7'),
    # path('test8/', views.test8, name='test8'),
    # path('test9/', views.test9, name='test9'),
    # path('test10/<username>/', views.test10, name='test10'),
    # path('test11/', views.test11, name='test11'),
    # path('test12/', views.test12, name='test12'),
    # path('test13/', views.test13, name='test13'),
    # re_path(r'^test14/', views.test14, name='test14'),
    # re_path(r'^test15/', test15, name='test15'),
    # re_path(r'^.*\.*', views.test16, name='test16'),
    # re_path(r'^test17/', views.test17, name='test17'),
    # path('test18/', views.test18, name='test18'),
    # path('test19/', views.test19, name='test19'),
    # path('test20/', views.test20, name='test20'),
    path('', views.test21, name='test21'),
    path('delete/<delete_id>/', views.delete, name='delete'),
    path('<edit_id>/change/', views.edit, name='edit'),
    path('news/<slug>/', views.news, name='news'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
