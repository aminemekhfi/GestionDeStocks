from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestionDeStock/',include('base.urls')),  
    path('membres/',include('django.contrib.auth.urls')),  
    path('membres/',include('membres.urls')),  
]
