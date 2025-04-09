"""Test URL patterns for organizations app."""
#
# from django.urls import resolve, reverse
#
#
# def test_organizations_list():
#     """Test organizations list view."""
#     assert reverse("organizations:list_view") == f"/api/organizations/"
#     assert resolve("/api/organizations/").view_name == "organizations:list_view"
#
#
# def test_oraganizations_datail():
#     """Test organizations detail view."""
#     pk = 1
#     assert (
#         reverse("organizations:detail_view", kwargs={"pk": pk})
#         == f"/api/organizations/{pk}/"
#     )
#     assert resolve(f"/api/organizations/{pk}/").view_name == "organizations:detail_view"
