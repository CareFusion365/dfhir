"""Encounter filter module."""

from django_filters import DateTimeFromToRangeFilter
from django_filters import rest_framework as filters

from .models import Encounter


class EncounterFilter(filters.FilterSet):
    """Encounter filter."""

    id = filters.CharFilter(field_name="id", lookup_expr="iexact")
    start_date_time = DateTimeFromToRangeFilter(
        field_name="start_date_time", lookup_expr="gte"
    )
    end_date_time = DateTimeFromToRangeFilter(
        field_name="end_date_time", lookup_expr="lte"
    )
    patient = filters.CharFilter(
        field_name="subject__actor__display", lookup_expr="icontains"
    )
    practitioner = filters.CharFilter(
        field_name="encounter_participant__practitioner__id", lookup_expr="iexact"
    )

    class Meta:
        """Meta class."""

        model = Encounter
        fields = ["id", "start_date_time", "end_date_time", "patient", "practitioner"]
