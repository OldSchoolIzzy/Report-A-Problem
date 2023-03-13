from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('register/',views.registerPage),
    path('login/', views.loginPage)
]