from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('linkchecker.urls')),  # Include the linkchecker app's URLs
]
