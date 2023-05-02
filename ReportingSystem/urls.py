from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('issue/', views.issues, name="issues"),
    path('cleaniness/', views.cleaniness, name="cleaniness"),
    path('electrical/',views.electrical, name="electrcial"),
    path('hazards/',views.hazards, name="hazards"),
    path('hvac/', views.hvac, name="hvac"),
    path('it/', views.it, name="it"),
    path('pest/', views.pest, name="pest"),
    path('plumbing/', views.plumbing, name="plumbing"),
    path('restroom', views.restroom, name="restroom"),
    path('create/', views.create_ticket_2, name='create_ticket_2'),
    path('viewticket/', views.ticket_view, name='ticket_view'),



]