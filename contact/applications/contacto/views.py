from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    TemplateView, 
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    View,
)

from .models import Cliente
#
from .utils import render_to_pdf
#forms
from .forms import ContactoForm

from django.urls import reverse_lazy

class InicioView(TemplateView):
    """ Vista que carga la página de inicio """
    template_name = 'inicio.html'
    
    
class ListContacto(ListView):
    template_name = 'contacto/list_all.html'
    paginate_by = 4
    ordering = 'nombre'
    #model = Cliente
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Cliente.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista
    
    
class ContactoDetailView(DetailView):
    template_name = 'contacto/detail_contacto.html'
    model = Cliente
    
    def get_context_data(self, **kwargs):
        context = super(ContactoDetailView, self).get_context_data(**kwargs)
        context['nombre'] = 'Contactos del mes'
        return context
    
    
class ListContacto2(ListView):
    template_name = 'contacto/list2_all.html'
    paginate_by = 4
    ordering = 'nombre'
    #model = Cliente
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Cliente.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista


class ContactoUpdateView(UpdateView):
    template_name = 'contacto/update.html'
    model = Cliente
    fields = [
        'nombre',
        'apellidos',
        'profesion',
        'foto',
        'telefono',
        'direccion',
        'ciudad',
    ]
    success_url = reverse_lazy('contactos_app:contactos_all')


class ContactoCreateView(CreateView):
    template_name = 'contacto/create.html'
    #model = Cliente
    form_class = ContactoForm
    success_url = reverse_lazy('contactos_app:contactos_all')
    
    
class ContactoDeleteView(DeleteView):
    template_name = 'contacto/delete.html'
    model = Cliente 
    success_url = reverse_lazy('contactos_app:contactos_all')
    
    
# GENERADOR PDF CON DJANGO - HTML a PDF
class ListaContactos(ListView):
    model = Cliente
    template_name = 'contacto/contactos.html'
    context_object_name = 'contactos'

class ListContactosPdf(View):

    def get(self, request, *args, **kwargs):
        contactos = Cliente.objects.all()
        data = {
            'count': contactos.count(),
            'contactos': contactos
        }
        pdf = render_to_pdf('contacto/lista.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    


    
    

