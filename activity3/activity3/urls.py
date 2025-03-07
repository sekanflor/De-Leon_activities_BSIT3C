from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  


def redirect_to_api(request):
    return redirect('/api/items/')  

urlpatterns = [
    path('', redirect_to_api), 
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
]
