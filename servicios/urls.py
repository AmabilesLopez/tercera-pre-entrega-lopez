from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_instalacion/', views.registrar_instalacion, name='registrar_instalacion'),
    path('lista_instalaciones/', views.lista_instalaciones, name='lista_instalaciones'),
    path('instalacion/<int:pk>/', views.detalle_instalacion, name='detalle_instalacion'),
]
