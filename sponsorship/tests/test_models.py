# mpesa/tests/test_models.py

from django.test import TestCase

from sponsorship.models import *


class TestApplicantModel(TestCase):
    def setUp(self):
        self.applicant = Applicant(
            applicant_name='Pay Bill',
            applicant_address='NL321HAW66',
            applicant_phone="0706449682",
            applicant_email="mutahijames0@gmail.com",
            applicant_birth_cert='601479',
            applicant_national_id='Sample1',
        )
        self.applicant.save()

    def test_category_creation(self):
        self.assertEqual(Applicant.objects.count(), 1)

    def test_category_representation(self):
        self.assertEqual(self.applicant.applicant_name, str(self.applicant))
