"""Tests for base (and related) serializers using payloads in tests/base/payloads."""

from __future__ import annotations

import json
import os
from typing import Any, Dict

import pytest
from django.db import connection

from dfhir.base import serializers as base_s
from dfhir.healthcareservices.serializers import ServiceTypeSerializer

# Skip DB-backed serializer tests unless running on PostgreSQL, because ArrayField requires it
pytestmark = pytest.mark.skipif(
    connection.vendor != "postgresql",
    reason="Serializer tests require PostgreSQL (ArrayField).",
)


PAYLOADS_DIR = os.path.join(os.path.dirname(__file__), "payloads")


def _load_payload(name: str) -> Dict[str, Any]:
    with open(os.path.join(PAYLOADS_DIR, name), "r", encoding="utf-8") as fh:
        return json.load(fh)


@pytest.mark.parametrize(
    "payload_file,serializer_cls",
    [
        ("address.json", base_s.AddressSerializer),
        ("age.json", base_s.AgeSerializer),
        ("annotation.json", base_s.AnnotationSerializer),
        ("attachment.json", base_s.AttachmentSerializer),
        ("availability.json", base_s.AvailabilitySerializer),
        ("available_time.json", base_s.AvailableTimeSerializer),
        ("codeable_concept.json", base_s.CodeableConceptSerializer),
        ("codeable_reference.json", base_s.CodeableReferenceSerializer),
        ("coding.json", base_s.CodingSerializer),
        ("communication.json", base_s.CommunicationSerializer),
        ("contact_detail.json", base_s.ContactDetailSerializer),
        ("contact_point.json", base_s.ContactPointSerializer),
        ("duration.json", base_s.DurationSerializer),
        ("expression.json", base_s.ExpressionSerializer),
        ("extended_contact_detail.json", base_s.ExtendedContactDetailSerializer),
        ("human_name.json", base_s.HumanNameSerializer),
        ("identifier.json", base_s.IdentifierSerializer),
        ("monetary_component.json", base_s.MonetaryComponentSerializer),
        ("money.json", base_s.MoneySerializer),
        ("not_available_time.json", base_s.NotAvailableTimeSerializer),
        ("organization_reference.json", base_s.OrganizationReferenceSerializer),
        ("payload.json", base_s.PayloadSerializer),
        ("period.json", base_s.PeriodSerializer),
        ("product_shelf_life.json", base_s.ProductShelfLifeSerializer),
        ("qualification.json", base_s.QualificationSerializer),
        ("quantity.json", base_s.QuantitySerializer),
        ("range.json", base_s.RangeSerializer),
        ("ratio.json", base_s.RatioSerializer),
        ("reference.json", base_s.ReferenceSerializer),
        ("related_artifact.json", base_s.RelatedArtifactSerializer),
        ("relative_time.json", base_s.RelativeTimeSerializer),
        ("repeat.json", base_s.RepeatSerializer),
        ("simple_quantity.json", base_s.SimpleQuantitySerializer),
        ("timing.json", base_s.TimingSerializer),
        ("trigger_definition.json", base_s.TriggerDefinitionSerializer),
        ("usage_context.json", base_s.UsageContextSerializer),
        (
            "virtual_service_detail_address.json",
            base_s.VirtualServiceDetailAddressSerializer,
        ),
        ("virtual_service_details.json", base_s.VirtualServiceDetailsSerializer),
        ("service_type.json", ServiceTypeSerializer),
    ],
)
@pytest.mark.django_db()
def test_payload_validates_and_saves(
    payload_file: str,
    serializer_cls,
    fhir_refs,
):
    data = _load_payload(payload_file)
    serializer = serializer_cls(data=data)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert getattr(instance, "pk", None) is not None
    assert (
        getattr(instance, "resource_type", instance.__class__.__name__)
        == instance.__class__.__name__
    )


@pytest.mark.django_db()
def test_organization_reference_parsing(fhir_refs):
    """Test organization_reference parsing."""
    payload = _load_payload("organization_reference.json")
    serializer = base_s.OrganizationReferenceSerializer(data=payload)
    assert serializer.is_valid(), serializer.errors
    obj = serializer.save()
    assert obj.organization_id == 1


@pytest.mark.django_db()
def test_signature_references(fhir_refs):
    payload = _load_payload("signature.json")
    serializer = base_s.SignatureSerializer(data=payload)
    assert serializer.is_valid(), serializer.errors
    sig = serializer.save()
    assert sig.who is not None
    assert getattr(sig.who, "practitioner_id", None) == 1


assert True
