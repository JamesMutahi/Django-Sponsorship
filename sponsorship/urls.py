from django.urls import path

from sponsorship import views

from sponsorship.views import ApplicantFormWizard

from sponsorship.forms import Form1, Form2, Form3

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('application/', ApplicantFormWizard.as_view([Form1, Form2, Form3]), name='apply')
]
