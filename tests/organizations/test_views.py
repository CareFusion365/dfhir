"""Test cases for the organizations views."""

import json
import os

from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from dfhir.organizations.models import Organization
from dfhir.organizations.serializers import OrganizationSerializer
from dfhir.organizations.views import OrganizationDetailView, OrganizationListView


class TestOrganizationViews(APITestCase):
    """Test Organization views."""

    def load_payload(self):
        """Load payload from JSON file."""
        payload_path = os.path.join(os.path.dirname(__file__), "payload.json")
        with open(payload_path, "r") as file:
            return json.load(file)

    def setUp(self):
        """Set up test data."""
        self.factory = APIRequestFactory()
        self.payload_data = self.load_payload()
        self.serializer = OrganizationSerializer(data=self.payload_data)
        self.serializer.is_valid(raise_exception=True)
        self.organization = self.serializer.save()

    def test_organization_list_view(self):
        """Test organization list view."""
        url = reverse("organizations:list_view")
        request = self.factory.get(url)
        view = OrganizationListView.as_view()
        response = view(request)
        assert response.status_code == 200
        assert len(response.data) >= 1

    def test_organization_detail_view(self):
        """Test organization detail view."""
        url = reverse("organizations:detail_view", kwargs={"pk": self.organization.pk})
        request = self.factory.get(url)
        view = OrganizationDetailView.as_view()
        response = view(request, pk=self.organization.pk)
        assert response.status_code == 200
        assert response.data["id"] == self.organization.id

    def test_organization_detail_view_not_found(self):
        """Test organization detail view for non-existing organization."""
        url = reverse("organizations:detail_view", kwargs={"pk": 9999})
        request = self.factory.get(url)
        view = OrganizationDetailView.as_view()
        response = view(request, pk=9999)
        assert response.status_code == 404

    def test_organization_list_view_empty(self):
        """Test organization list view when no organizations exist."""
        Organization.objects.all().delete()
        url = reverse("organizations:list_view")
        request = self.factory.get(url)
        view = OrganizationListView.as_view()
        response = view(request)
        assert response.status_code == 200
        assert len(response.data) == 0

    def test_organization_patch_view(self):
        """Test organization patch view."""
        url = reverse("organizations:detail_view", kwargs={"pk": self.organization.pk})
        patch_data = {"name": "Updated Organization Name"}
        request = self.factory.patch(url, data=patch_data, format="json")
        view = OrganizationDetailView.as_view()
        response = view(request, pk=self.organization.pk)
        assert response.status_code == 200
        assert response.data["name"] == "Updated Organization Name"

    def test_organization_delete_view(self):
        """Test organization delete view."""
        url = reverse("organizations:detail_view", kwargs={"pk": self.organization.pk})
        request = self.factory.delete(url)
        view = OrganizationDetailView.as_view()
        response = view(request, pk=self.organization.pk)
        assert response.status_code == 204

        get_request = self.factory.get(url)
        get_response = view(get_request, pk=self.organization.pk)
        assert get_response.status_code == 404
