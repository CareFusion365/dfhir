"""appointment filters."""

from django_filters import DateFromToRangeFilter
from django_filters import rest_framework as filters

from dfhir.appointments.models import Appointment


class AppointmentFilter(filters.FilterSet):
    """appointment filter."""

    id = filters.CharFilter(field_name="id", lookup_expr="iexact")
    status = filters.CharFilter(field_name="status", lookup_expr="icontains")
    start = DateFromToRangeFilter(field_name="start", lookup_expr="gte")
    end = DateFromToRangeFilter(field_name="end", lookup_expr="lte")
    subject = filters.CharFilter(
        field_name="subject__patient__id", lookup_expr="iexact"
    )
    participant = filters.CharFilter(
        field_name="participant__actor__practitioner__id", lookup_expr="icontains"
    )

    class Meta:
        """meta options."""

        model = Appointment
        fields = [
            "id",
            "status",
            "start",
            "end",
            "subject",
            "participant",
        ]
