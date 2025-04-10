"""Test Organization model."""
#
# from django.contrib.auth import get_user_model
# from django.test import TestCase
#
# from dfhir.organizations.models import Organization
#
#
# class TestOrganizationModel(TestCase):
#     """Test Organization model."""
#
#     def test_create(self):
#         """Test create organization."""
#         organization = Organization.objects.create(
#             name="Test Organization",
#             website="http://test.com",
#             email="example@mail.com",
#             phone_number="+1234567890",
#         )
#         organization.admin = get_user_model().objects.create(
#             email="admin@mail.com", username="admin", password="asdf"
#         )
#         organization.save()
#
#         assert Organization.objects.count() == 1
#         assert Organization.objects.get().name == "Test Organization"
#         assert Organization.objects.get().website == "http://test.com"
#         assert Organization.objects.get().admin.email == "admin@mail.com"
#         assert Organization.objects.get().admin.username == "admin"
#         assert type(Organization.objects.get().pk) is int
