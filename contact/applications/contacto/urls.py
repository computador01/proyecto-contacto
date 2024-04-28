from django.urls import path

from .import views

app_name = "contactos_app"

urlpatterns = [
    path('', views.InicioView.as_view(), 
             name='inicio'), 
    
    path('listar-contactos/', views.ListContacto.as_view(), 
             name='contactos_all'), 
    
    path('ver-contactos/<pk>/', views.ContactoDetailView.as_view(), 
             name='contactos_detail'), 
    
    path('listar-contactos2/', views.ListContacto2.as_view(), 
             name='contactos2_all'), 
    
    path('contactos-update/<pk>/', views.ContactoUpdateView.as_view(), 
             name='update'), 
    
    path('contactos-create/', views.ContactoCreateView.as_view(), 
             name='create'), 
    
    path('contactos-delete/<pk>/', views.ContactoDeleteView.as_view(), 
             name='delete'), 
    
    path('lista/', views.ListaContactos.as_view(), 
             name='lista'), 
    
    path('lista_contactos/', views.ListContactosPdf.as_view(), 
             name='listarpdf'),
]