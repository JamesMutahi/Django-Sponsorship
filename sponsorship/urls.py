from django.urls import path

from sponsorship import views

from sponsorship.views import *

from sponsorship.forms import Form1, Form2, Form3

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('applications/', ApplicationsListView.as_view(), name='applications'),
    path('application/', ApplicantFormWizard.as_view([Form1, Form2, Form3]), name='apply'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<int:pk>/update/', ApplicantUpdateView.as_view(), name='application-update'),
]
