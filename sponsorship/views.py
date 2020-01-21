from django.shortcuts import render


def home(request):
    return render(request, 'sponsorship/home.html')


def apply(request):
    return render(request, 'sponsorship/apply.html')
