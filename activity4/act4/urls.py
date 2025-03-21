from django.urls import path
from .views import index
app_name = "act4"
urlpatterns = [
path('', index, name='index'),
]
