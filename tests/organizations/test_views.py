"""Test cases for the organizations views."""

from rest_framework import status
from rest_framework.test import APIRequestFactory

from dfhir.organizations.models import Organization
from dfhir.organizations.views import OrganizationDetailView, OrganizationListView

from . import OrganizationTestSetup


class TestOrganizationListView(OrganizationTestSetup):
    """Test organization list view."""

    def test_get(self):
        """Test get request."""
        factory = APIRequestFactory()
        request = factory.get("/api/organizations/")
        view = OrganizationListView.as_view()
        response = view(request)
        assert response.status_code == status.HTTP_200_OK

    def test_post(self):
        """Test post request."""
        factory = APIRequestFactory()
        request = factory.post("/api/organizations/", self.serializer.validated_data)
        view = OrganizationListView.as_view()
        response = view(request)

        assert response.status_code == status.HTTP_200_OK
        assert self.serializer.data["name"] == self.organization.name
        assert response.data["name"] == self.organization.name
        assert response.data["name"] == self.serializer.data["name"]


class TestOrganizationDetailView(OrganizationTestSetup):
    """Test organization detail view."""

    def test_get_organization(self):
        """Test get request."""
        organization = Organization.objects.create(name="Test Organization")
        factory = APIRequestFactory()
        request = factory.get(f"/api/organizations/{organization.pk}/")
        view = OrganizationDetailView.as_view()
        response = view(request, pk=organization.pk)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == organization.name
        assert response.data["id"] == organization.pk

    def test_patch_organization(self):
        """Test patch request."""
        organization = Organization.objects.create(name="Test Organization")
        factory = APIRequestFactory()
        request = factory.patch(
            f"/api/organizations/{organization.pk}/", {"name": "Updated Organization"}
        )
        view = OrganizationDetailView.as_view()
        response = view(request, pk=organization.pk)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Updated Organization"

    def test_delete_organization(self):
        """Test delete request."""
        organization = Organization.objects.create(name="Test Organization")
        factory = APIRequestFactory()
        request = factory.delete(f"/api/organizations/{organization.pk}/")
        view = OrganizationDetailView.as_view()
        response = view(request, pk=organization.pk)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None
        assert Organization.objects.filter(pk=organization.pk).exists() is False
