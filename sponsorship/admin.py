from django.contrib import admin
from sponsorship.models import Applicant

# Register your models here.
admin.site.site_header = "Sponsorships Admin"
admin.site.site_title = "Sponsorships Admin"

admin.site.register(Applicant)
