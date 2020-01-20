from django.db import models


class Applicant(models.Model):
    applicant_name = models.CharField(max_length=255)
    applicant_address = models.CharField(max_length=255)
    applicant_phone = models.IntegerField()
    applicant_email = models.EmailField()
    applicant_birth_cert = models.FileField(upload_to="")
    applicant_national_id = models.FileField()

    def __str__(self):
        return self.applicant_name


class ApplicantSchoolInfo(models.Model):
    id = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name="applicant_school_info",
                              primary_key=True)
    school_name = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)
    academic_level = models.CharField(max_length=255)
    year_of_completion = models.DateField()

    def __str__(self):
        return self.id


class Reasons(models.Model):
    id = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name="reasons",
                              primary_key=True)
    reasons = models.TextField()
    recommendation_letter = models.FileField()

    def __str__(self):
        return self.id
