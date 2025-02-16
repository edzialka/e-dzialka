from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/plots/', include('plots.urls')),
    path('api/gardens/', include('gardens.urls')),
]
