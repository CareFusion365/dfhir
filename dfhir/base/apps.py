"""base app."""

from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """base app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "dfhir.base"
    verbose_name = _("Base")
