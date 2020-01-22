from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
)

from sponsorship.models import Applicant


def home(request):
    return render(request, 'sponsorship/home.html')


def about(request):
    applications = Applicant.objects.all()
    return render(request, 'sponsorship/about.html', {"applications": applications})


class ApplicantFormWizard(SessionWizardView):
    template_name = 'sponsorship/application_form.html'
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'temp'))

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        form_data = form_data
        print(form_data)
        an_application = Applicant.objects.create(
            applicant_name=form_data[0]["applicant_name"],
            applicant_address=form_data[0]["applicant_address"],
            applicant_phone=form_data[0]["applicant_phone"],
            applicant_email=form_data[0]["applicant_email"],
            applicant_birth_cert=form_data[0]["applicant_birth_cert"],
            applicant_national_id=form_data[0]["applicant_national_id"],
            school_name=form_data[1]["school_name"],
            school_address=form_data[1]["school_address"],
            academic_level=form_data[1]["academic_level"],
            year_of_completion=form_data[1]["year_of_completion"],
            reasons=form_data[2]["reasons"],
            recommendation_letter=form_data[2]["recommendation_letter"],
        )
        print(an_application)
        return render(self.request, 'sponsorship/done.html', {"form_data": form_data})


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    # email = form_data[0]['applicant_email']
    # print(email)
    # send_mail(
    #     'SPONSORSHIP',
    #     'You have applied for sponsorship',
    #     "{EMAIL_HOST_USER}",
    #     ['{email}'.format(email=email)],
    #     fail_silently=True,
    # )
    # print(form_data)
    return form_data


class ApplicationsListView(ListView, LoginRequiredMixin):
    model = Applicant
    template_name = 'sponsorship/application_view.html'
    context_object_name = 'applications'
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.groups.filter(name='sponsor').exists():
            return Applicant.objects.filter(valid=True).order_by('-date_posted')
        else:
            return Applicant.objects.all().order_by('-date_posted')


class ApplicationDetailView(DetailView, LoginRequiredMixin):
    model = Applicant
    template_name = 'sponsorship/application_detail.html'


class ApplicantUpdateView(UpdateView, LoginRequiredMixin):
    model = Applicant
    template_name = 'sponsorship/application_update.html'
    fields = ['valid']

    def form_valid(self, form):
        return form
