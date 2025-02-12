from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userdata.urls')),  # Includes all URLs from userdata/urls.py under /user/
]
