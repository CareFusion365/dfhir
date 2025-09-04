"""Test URL patterns for organizations app."""

from django.urls import resolve

from . import OrganizationTestSetup


class TestOrganizationsURLs(OrganizationTestSetup):
    """Test URL patterns for organizations app."""

    def test_organizations_list(self):
        """Test organizations list view."""
        assert (
            resolve("/api/organizations/").func.view_class.__name__
            == "OrganizationListView"
        )

    def test_oraganizations_datail(self):
        """Test organizations detail view."""
        pk = 1
        assert (
            resolve(f"/api/organizations/{pk}/").func.view_class.__name__
            == "OrganizationDetailView"
        )
