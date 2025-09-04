"""Test Organization model."""

from . import OrganizationTestSetup


class TestOrganizationModel(OrganizationTestSetup):
    """Test Organization model."""

    def test_create_organization(self):
        """Test create organization."""
        assert self.serializer.data["name"] == self.organization.name
        assert self.serializer.data["alias"] == self.organization.alias
        assert self.serializer.data["website"] == self.organization.website
        assert self.serializer.data["email"] == self.organization.email
        assert self.serializer.data["status"] == self.organization.status
        assert self.serializer.data["active"] == self.organization.active

        assert self.serializer.data["part_of"] == self.organization.part_of
        assert self.serializer.data["description"] == self.organization.description
        assert self.serializer.data["id"] == self.organization.pk
