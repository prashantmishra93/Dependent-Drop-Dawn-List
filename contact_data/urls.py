from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('add/', views.PersonAddView.as_view(), name='add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
]