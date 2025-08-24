"""appointment filters."""

from django_filters import DateFromToRangeFilter
from django_filters import rest_framework as filters

from dfhir.appointments.models import Appointment


class AppointmentFilter(filters.FilterSet):
    """appointment filter."""

    id = filters.CharFilter(field_name="id", lookup_expr="iexact")
    status = filters.CharFilter(field_name="statud", lookup_expr="icontains")
    start = DateFromToRangeFilter(field_name="start", lookup_expr="gte")
    end = DateFromToRangeFilter(field_name="end", lookup_expr="lte")
    service_type = filters.CharFilter(
        field_name="service_type", lookup_expr="icontains"
    )
    reason = filters.CharFilter(field_name="reason", lookup_expr="icontains")
    description = filters.CharFilter(field_name="description", lookup_expr="icontains")
    subject = filters.CharFilter(field_name="subject", lookup_expr="icontains")
    participant = filters.CharFilter(field_name="participant", lookup_expr="icontains")

    class Meta:
        """meta options."""

        model = Appointment
        fields = [
            "id",
            "status",
            "start",
            "end",
            "service_type",
            "reason",
            "description",
            "subject",
            "participant",
        ]
