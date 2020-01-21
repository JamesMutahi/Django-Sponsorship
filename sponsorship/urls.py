from django.urls import path

from sponsorship import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
]
