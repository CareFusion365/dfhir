import json
import os
from typing import Any, Dict

import pytest


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):  # noqa: PT004
    # Implicitly enable DB for all tests in this package
    pass


@pytest.fixture()
def fhir_refs(django_db_blocker):
    """Create minimal external resources required by BaseReference serializers.

    Ensures integer IDs (1) exist for Organization, Practitioner, and Patient so that
    payloads using e.g. "Organization/1" validate successfully.
    """
    with django_db_blocker.unblock():
        # Import models lazily to avoid Django setup issues
        from dfhir.organizations.models import Organization
        from dfhir.patients.models import Patient
        from dfhir.practitioners.models import Practitioner

        # Create or get records with explicit primary keys = 1
        org, _ = Organization.objects.get_or_create(
            id=1, defaults={"name": "Good Health Clinic"}
        )
        prac, _ = Practitioner.objects.get_or_create(id=1)
        pat, _ = Patient.objects.get_or_create(id=1)
        return {"organization": org, "practitioner": prac, "patient": pat}


@pytest.fixture()
def load_payload() -> Any:
    """Helper to load a payload JSON by file name from tests/base/payloads."""
    base_dir = os.path.join(os.path.dirname(__file__), "base", "payloads")

    def _loader(name: str) -> Dict[str, Any]:
        path = os.path.join(base_dir, name)
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)

    return _loader


def _normalize_reference_dict_to_pk(value: Any) -> Any:
    """Convert {"reference": "Resource/1"} to integer 1 when needed.

    Some serializers (e.g., ExtendedContactDetail.organization) expect a PK integer,
    while our payloads use FHIR-style reference objects. This normalizer makes the
    payloads compatible with those serializer expectations without altering the files.
    """
    if (
        isinstance(value, dict)
        and "reference" in value
        and isinstance(value["reference"], str)
    ):
        parts = value["reference"].split("/")
        if len(parts) == 2 and parts[1].isdigit():
            return int(parts[1])
    return value


@pytest.fixture()
def normalize_payload_for_serializer():
    """Return a function to minimally adapt payloads for serializer expectations.

    Applies conservative fixes only where serializers require primary-key integers
    instead of reference dicts (e.g., ExtendedContactDetail.organization).
    """

    def _normalize(name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        # ExtendedContactDetailSerializer expects a PK for `organization` (FK to Organization),
        # but payload provides {"reference": "Organization/1"}.
        if name == "extended_contact_detail.json" and "organization" in data:
            data = {
                **data,
                "organization": _normalize_reference_dict_to_pk(data["organization"]),
            }
        return data

    return _normalize
