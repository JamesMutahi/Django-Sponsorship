from django.db import models


class Applicant(models.Model):
    applicant_name = models.CharField(max_length=255)
    applicant_address = models.CharField(max_length=255)
    applicant_phone = models.IntegerField()
    applicant_email = models.EmailField()
    applicant_birth_cert = models.FileField(upload_to="birth_certs")
    applicant_national_id = models.FileField(upload_to="national_ids")
    school_name = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)
    academic_level = models.CharField(max_length=255)
    year_of_completion = models.DateField()
    reasons = models.TextField()
    recommendation_letter = models.FileField(upload_to="recommendation_letters")

    def __str__(self):
        return self.applicant_name

