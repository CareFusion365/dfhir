"""Test cases for the organizations views."""

# TODO: need to fix tests
import pytest
from rest_framework.test import APIRequestFactory

from dfhir.organizations.models import Organization
from dfhir.organizations.views import OrganizationDetailView, OrganizationListView


@pytest.mark.django_db
def test_get_all_organizations_endpoint():
    """Test get request."""
    factory = APIRequestFactory()
    request = factory.get("/api/organizations/")
    view = OrganizationListView.as_view()
    response = view(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_organization_endpoint():
    """Test post request."""
    factory = APIRequestFactory()
    request = factory.post("/api/organizations/", {"name": "Test Organization"})
    view = OrganizationListView.as_view()
    response = view(request)
    assert response.status_code == 200
    assert Organization.objects.count() == 1
    assert Organization.objects.get().name == "Test Organization"


@pytest.mark.django_db
def test_get_one_organization_endpoint():
    """Test get request."""
    organization = Organization.objects.create(name="Test Organization")
    factory = APIRequestFactory()
    request = factory.get(f"/api/organizations/{organization.pk}/")
    view = OrganizationDetailView.as_view()
    response = view(request, pk=organization.pk)
    assert response.status_code == 200
    assert response.data["name"] == "Test Organization"


@pytest.mark.django_db
def test_patch_organization_endpoint():
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


@pytest.mark.django_db
def test_delete_organization_endpoint():
    """Test delete request."""
    organization = Organization.objects.create(name="Test Organization")
    factory = APIRequestFactory()
    request = factory.delete(f"/api/organizations/{organization.pk}/")
    view = OrganizationDetailView.as_view()
    response = view(request, pk=organization.pk)
    assert response.status_code == 204
    assert Organization.objects.count() == 0
    assert Organization.objects.exists() is False
