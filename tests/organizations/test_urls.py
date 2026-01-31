"""Test URL patterns for organizations app."""

from django.test import TestCase
from django.urls import resolve, reverse


class TestOrganizationUrls(TestCase):
    """Test URL patterns for organizations app."""

    def test_organizations_list(self):
        """Test organizations list view."""
        assert reverse("organizations:list_view") == f"/api/organizations/"
        assert resolve("/api/organizations/").view_name == "organizations:list_view"

    def test_organizations_detail(self):
        """Test organizations detail view."""
        pk = 1
        assert (
            reverse("organizations:detail_view", kwargs={"pk": pk})
            == f"/api/organizations/{pk}/"
        )
        assert (
            resolve(f"/api/organizations/{pk}/").view_name
            == "organizations:detail_view"
        )
