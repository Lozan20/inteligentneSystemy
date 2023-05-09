from django.contrib import admin
from django.urls import path, include
from car_repair_app.views import recommendations

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("recommendations/", recommendations),
]
