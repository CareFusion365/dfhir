"""organization tests."""

import pytest

from dfhir.organizations.models import Organization


@pytest.mark.django_db
def test_organization_create():
    """Fixture for organization model."""
    organization = Organization.objects.create(
        name="Burgers University Medical Center",
        alias=["Burgers University Medical Center"],
        email="bumc@gmail.com",
        website="www.bumc.com",
        active=True,
    )
    assert organization.name == "Burgers University Medical " "Center"
    assert organization.alias == ["Burgers University " "Medical Center"]
    assert organization.email == "bumc@gmail.com"
    assert organization.website == "www.bumc.com"
    assert organization.active
    assert Organization.objects.count() == 1
