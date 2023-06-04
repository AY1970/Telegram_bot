from django.urls import path
from . import views

urlpatterns = [
    path('commands/', views.commands_view, name='commands'),
    path('add_contact/', views.add_contact_view, name='add_contact'),
    path('view_contacts/', views.view_contacts_view, name='view_contacts'),
    path('delete_contact/', views.delete_contact_view, name='delete_contact'),
    path('weather/', views.weather_view, name='weather'),
]
