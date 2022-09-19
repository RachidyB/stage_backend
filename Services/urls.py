from django.urls import path
from .Views import Technician, Voiture, Service

urlpatterns = [
    #technician
    path('Technician-list/', Technician.ShowAll, name='Technician-list'),
    path('Technician-by-id/<int:pk>/',  Technician.ViewTechnicianById, name='Technician-by-id'),
    path('Technician-by-name/<nom>/',  Technician.ViewTechnicianByName, name='Technician-by-name'),
    path('Technician-by-profession/<profession>/',  Technician.ViewTechnicianByProfession, name='Technician-by-profession'),
    path('Technician-create/',  Technician.CreateTechnician, name='Technician-create'),
    path('Technician-update/<pk>/',  Technician.updateTechnician, name='Technician-update'),
    path('Technician-delete/<pk>',  Technician.deleteTechnician, name='Technician-delete'),
    #Voiture
    path('Voiture-list/',  Voiture.ShowAll, name='Voiture-list'),
    path('Voiture-by-matricule/<int:pk>/', Voiture.ViewVoitureBymatricule, name='Voiture-by-matricule'),
    path('Voiture-by-marque/<marque>/', Voiture.ViewVoitureByMarque, name='Voiture-by-Marque'),
    path('Voiture-create/',  Voiture.CreateVoiture, name='Voiture-create'),
    path('Voiture-update/<pk>/',  Voiture.updateVoiture, name='Voiture-update'),
    path('Voiture-delete/<pk>', Voiture.deleteVoiture, name='Voiture-delete'),
    #Service
    path('Service-list/', Service.ShowAll, name='Service-list'),
    path('Service-by-id/<int:pk>/', Service.ViewServiceById, name='Service-by-id'),
    path('Service-by-technician/<id>/', Service.ViewServiceByTechnicianId, name='Service-by-technician-id'),
    #path('Service-by-technician-Name/<nom>/', Service.ViewServiceByTechnicianName, name='Service-by-technician-name'),
    path('Service-by-voiture/<matricule>/', Service.ViewServiceByVoitureMatricule, name='Service-by-Voiture-id'),
    path('Service-by-date_entrée/<date>/', Service.ViewServiceByDateEntree, name='Service-by-date-entree'),
    path('Service-by-date_sortie/<date>/', Service.ViewServiceByDateSortie, name='Service-by-date-sortie'),
    path('Service-create/', Service.CreateService, name='Service-create'),
    path('Service-update/<pk>/', Service.updateService, name='Service-update'),
    path('Service-delete/<pk>', Service.deleteService, name='Service-delete'),

]