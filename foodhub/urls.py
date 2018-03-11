"""foodhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', views.list, name = 'restaurant_list'),
    path('details/<int:restaurant_id>/', views.detail, name="restaurant_detail"),
    path('create/', views.create, name="restaurant_create"),
    path('update/<int:restaurant_id>/', views.update, name="restaurant_update" ),
    path('delete/<int:restaurant_id>/', views.restaurant_delete, name='delete'),
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
    path('item_create/<int:restaurant_id>/', views.create_item, name="item_create"),
    path('favorite/<int:restaurant_id>/', views.favorite, name="favorite-button"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

