from django.contrib import admin
from django.urls import path, include

# from core.views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
