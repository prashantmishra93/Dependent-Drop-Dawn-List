from django.shortcuts import render
from .models import ContactUs, State, City
from .forms import ContactForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class ContactView(ListView):
    model = ContactUs
    context_object_name = 'peoples'
    template_name = 'contact_list.html'

class PersonAddView(CreateView):
    model = ContactUs
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('contact')

class PersonUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('contact')

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'hr/state_dropdown_list_options.html', {'states':states})