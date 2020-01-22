from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


def home(request):
    return render(request, 'sponsorship/home.html')


def about(request):
    return render(request, 'sponsorship/about.html')


class ApplicantFormWizard(SessionWizardView):
    template_name = 'sponsorship/application_form.html'
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'temp'))

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        form_data = form_data
        # print(form_data)

        return render(self.request, 'sponsorship/done.html', {"form_data": form_data})


def process_form_data(form_list):
    data = [form.cleaned_data for form in form_list]
    form_data = data[0]
    email = form_data['applicant_email']
    # print(email)
    send_mail(
        'SPONSORSHIP',
        'You have applied for sponsorship',
        "{EMAIL_HOST_USER}",
        ['{email}'.format(email=email)],
        fail_silently=True,
    )
    # print(form_data)
    return form_data
