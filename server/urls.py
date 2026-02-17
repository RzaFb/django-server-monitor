from django.urls import path
from .views import add_server, get_server, get_all_servers

urlpatterns = [
    path('server', add_server, name='add_server'),
    path('server/<int:id>', get_server, name='get_server'),
    path('server/all', get_all_servers, name='get_all_servers'),
]