from django import forms
import datetime

year_dropdown = []
current_year = datetime.datetime.now().year
for y in range(2011, current_year + 1):
    year_dropdown.append((y, y))


class Form1(forms.Form):
    applicant_name = forms.CharField(max_length=100)
    applicant_address = forms.CharField(max_length=100)
    applicant_phone = forms.IntegerField()
    applicant_email = forms.EmailField()
    applicant_birth_cert = forms.FileField()
    applicant_national_id = forms.FileField()


class Form2(forms.Form):
    school_name = forms.CharField(max_length=100)
    school_address = forms.CharField(max_length=100)
    academic_level = forms.CharField(max_length=100)
    year_of_completion = forms.ChoiceField(choices=year_dropdown, initial=current_year)


class Form3(forms.Form):
    reasons = forms.CharField(widget=forms.Textarea)
    recommendation_letter = forms.FileField()
