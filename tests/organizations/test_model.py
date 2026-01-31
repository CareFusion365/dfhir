"""organization tests."""

from django.test import TestCase

from dfhir.organizations.models import Organization


class TestOrganization(TestCase):
    """Test organization model."""

    def setUp(self):
        """Organization test setup."""
        self.organization = Organization.objects.create(
            name="Burgers University Medical Center",
            alias=["Burgers University Medical Center"],
            email="bumc@gmail.com",
            website="www.bumc.com",
            active=True,
        )

    def test_organization_fields(self):
        """Test organization name."""
        self.assertEqual(self.organization.name, "Burgers University Medical " "Center")
        self.assertEqual(
            self.organization.alias, ["Burgers University " "Medical Center"]
        )
        self.assertEqual(self.organization.email, "bumc@gmail.com")
        self.assertEqual(self.organization.website, "www.bumc.com")
        self.assertEqual(self.organization.active, True)
