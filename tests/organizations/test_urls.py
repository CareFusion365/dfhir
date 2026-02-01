"""Test URL patterns for organizations app."""

from django.urls import resolve, reverse


def test_organizations_list():
    """Test organizations list view."""
    url = reverse("organizations:list_view")
    assert url == f"/api/organizations/"

    resolver = resolve(url)
    assert resolver.view_name == "organizations:list_view"


def test_organizations_detail():
    """Test organizations detail view."""
    url = reverse("organizations:detail_view", kwargs={"pk": 1})
    assert url == f"/api/organizations/{1}/"

    resolver = resolve(url)
    assert resolver.view_name == "organizations:detail_view"
