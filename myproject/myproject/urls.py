from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include(('portfolio.urls', 'portfolio'), namespace="portfolio")), 
    path('', lambda request: redirect('portfolio/', permanent=True)),  # Redirect root to portfolio
]