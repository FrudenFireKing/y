from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_advertisements.urls')),
    path('top-sellers/', include('app_advertisements.urls'))
]
