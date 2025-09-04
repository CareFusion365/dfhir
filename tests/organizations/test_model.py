"""Test Organization model."""

from . import OrganizationTestSetup


class TestOrganizationModel(OrganizationTestSetup):
    """Test Organization model."""

    def test_create_organization(self):
        """Test create organization."""
        assert self.serializer.validated_data["name"] == self.organization.name
        assert self.serializer.validated_data["alias"] == self.organization.alias
        assert self.serializer.validated_data["contact"] == self.organization.contact
        assert self.serializer.validated_data["endpoint"] == self.organization.endpoint
