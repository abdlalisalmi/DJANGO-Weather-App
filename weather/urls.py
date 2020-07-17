from django.contrib import admin
from django.urls import path

from .views import home, API_used, contact


urlpatterns = [
    path('', home, name="home"),
    path('api/', API_used, name="api"),

    path('admin/', admin.site.urls),
]
