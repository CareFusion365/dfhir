"""test organization models."""

from django.test import TestCase

from dfhir.base.models import Identifier
from dfhir.organizations.choices import OrganizationStatus
from dfhir.organizations.models import Organization


class TestOrganizationModel(TestCase):
    """Test Organization model."""

    def setUp(self):
        """Set up test data."""
        self.identifier = Identifier.objects.create(
            system="http://example.com", value="12345"
        )
        self.organization = Organization.objects.create(
            name="Test Organization",
            email="test@example.com",
            website="https://www.testorg.com",
            status=OrganizationStatus.PENDING,
        )
        self.organization.identifier.add(self.identifier)

    def test_organization_creation(self):
        """Test organization creation."""
        self.assertEqual(self.organization.name, "Test Organization")
        self.assertEqual(self.organization.email, "test@example.com")
        self.assertEqual(self.organization.website, "https://www.testorg.com")
        self.assertEqual(self.organization.status, OrganizationStatus.PENDING)
        assert self.identifier in self.organization.identifier.all()
