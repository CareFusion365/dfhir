"""Test cases for the organizations views."""

# TODO: need to fix tests
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from dfhir.organizations.models import Organization
from dfhir.organizations.views import OrganizationDetailView, OrganizationListView


class TestOrganizationListView(TestCase):
    """Test organization list view."""

    def test_get(self):
        """Test get request."""
        factory = APIRequestFactory()
        request = factory.get("/api/organizations/")
        view = OrganizationListView.as_view()
        response = view(request)
        assert response.status_code == 200

    def test_post(self):
        """Test post request."""
        factory = APIRequestFactory()
        request = factory.post("/api/organizations/", {"name": "Test Organization"})
        view = OrganizationListView.as_view()
        response = view(request)
        assert response.status_code == 200
        assert Organization.objects.count() == 1
        assert Organization.objects.get().name == "Test Organization"


class TestOrganizationDetailView(TestCase):
    """Test organization detail view."""

    def test_get(self):
        """Test get request."""
        organization = Organization.objects.create(name="Test Organization")
        factory = APIRequestFactory()
        request = factory.get(f"/api/organizations/{organization.pk}/")
        view = OrganizationDetailView.as_view()
        response = view(request, pk=organization.pk)
        assert response.status_code == 200
        assert response.data["name"] == "Test Organization"

    def test_patch(self):
        """Test patch request."""
        organization = Organization.objects.create(name="Test Organization")
        factory = APIRequestFactory()
        request = factory.patch(
            f"/api/organizations/{organization.pk}/", {"name": "Updated Organization"}
        )
        view = OrganizationDetailView.as_view()
        response = view(request, pk=organization.pk)
        assert response.status_code == 200
        assert Organization.objects.get().name == "Updated Organization"

    def test_delete(self):
        """Test delete request."""
        organization = Organization.objects.create(name="Test Organization")
        factory = APIRequestFactory()
        request = factory.delete(f"/api/organizations/{organization.pk}/")
        view = OrganizationDetailView.as_view()
        response = view(request, pk=organization.pk)
        assert response.status_code == 204
        assert Organization.objects.count() == 0
        assert Organization.objects.exists() is False
