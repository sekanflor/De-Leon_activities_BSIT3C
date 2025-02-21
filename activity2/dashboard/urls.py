from django.urls import path
from .views import index, report_view, settings_view

app_name = "dashboard"

urlpatterns = [
    path('', index, name='dashboard'),
    path('report/', report_view, name='report'),
    path('settings/', settings_view, name='settings'),
]
