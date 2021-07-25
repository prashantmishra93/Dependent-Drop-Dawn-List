from django.contrib import admin
from .models import Country, State, City, ContactUs

# Register your models here.

admin.site.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['country', 'name']

admin.site.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['country', 'state', 'name']

admin.site.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'country', 'state', 'city']

