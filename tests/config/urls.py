# ruff: noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path(
        "api/",
        include("dfhir.organizations.urls", namespace="organizations"),
    ),
    path(
        "api/",
        include("dfhir.patients.urls", namespace="patients"),
    ),
    path(
        "api/",
        include("dfhir.practitioners.urls", namespace="practitioners"),
    ),
    path(
        "api/",
        include("dfhir.locations.urls", namespace="locations"),
    ),
    path(
        "api/",
        include("dfhir.paymentnotices.urls", namespace="paymentnotices"),
    ),
    path(
        "api/",
        include("dfhir.healthcareservices.urls", namespace="healthcareservices"),
    ),
    path(
        "api/",
        include("dfhir.schedules.urls", namespace="schedules"),
    ),
    path(
        "api/",
        include("dfhir.slots.urls", namespace="slots"),
    ),
    path("api/", include("dfhir.encounters.urls", namespace="encounters")),
    path(
        "api/",
        include("dfhir.appointments.urls", namespace="appointments"),
    ),
    path(
        "api/",
        include("dfhir.servicerequests.urls", namespace="servicerequests"),
    ),
    path(
        "api/", include("dfhir.diagnosticreports.urls", namespace="diagnosticreports")
    ),
    path("api/", include("dfhir.observations.urls", namespace="observations")),
    path("api/", include("dfhir.medications.urls", namespace="medications")),
    path(
        "api/",
        include("dfhir.medicationrequests.urls", namespace="medicationrequests"),
    ),
    path(
        "api/",
        include("dfhir.persons.urls", namespace="persons"),
    ),
    path(
        "api/",
        include("dfhir.relatedpersons.urls", namespace="relatedpersons"),
    ),
    path(
        "api/",
        include("dfhir.careteams.urls", namespace="careteams"),
    ),
    path(
        "api/",
        include(
            "dfhir.medicationadministrations.urls",
            namespace="medicationadministrations",
        ),
    ),
    path(
        "api/",
        include("dfhir.episodeofcare.urls", namespace="episodeofcare"),
    ),
    path(
        "api/",
        include("dfhir.devicemetrics.urls", namespace="devicemetrics"),
    ),
    path(
        "api/",
        include("dfhir.medicationdispenses.urls", namespace="medicationdispenses"),
    ),
    path(
        "api/",
        include("dfhir.devicedefinitions.urls", namespace="devicedefinitions"),
    ),
    path(
        "api/",
        include("dfhir.flags.urls", namespace="flags"),
    ),
    path(
        "api/",
        include("dfhir.devices.urls", namespace="devices"),
    ),
    path(
        "api/",
        include("dfhir.personalrelationships.urls", namespace="personalrelateionships"),
    ),
    path(
        "api/",
        include("dfhir.substances.urls", namespace="substances"),
    ),
    path(
        "api/",
        include(
            "dfhir.observationdefinitions.urls", namespace="observationdefinitions"
        ),
    ),
    path(
        "api/",
        include(
            "dfhir.organizationaffiliations.urls", namespace="organizationaffiliations"
        ),
    ),
    path(
        "api/",
        include("dfhir.groups.urls", namespace="groups"),
    ),
    path(
        "api/",
        include("dfhir.endpoints.urls", namespace="endpoints"),
    ),
    path(
        "api/",
        include("dfhir.procedures.urls", namespace="procedures"),
    ),
    path(
        "api/",
        include("dfhir.enrollmentrequests.urls", namespace="enrollmentrequests"),
    ),
    path(
        "api/",
        include("dfhir.clinicalimpressions.urls", namespace="clinicalimpressions"),
    ),
    path("api/", include("dfhir.inventoryitems.urls", namespace="inventoryitems")),
    path(
        "api/",
        include("dfhir.visionprescriptions.urls", namespace="visionprescriptions"),
    ),
    path(
        "api/",
        include(
            "dfhir.coverageeligibilityrequests.urls",
            namespace="coverageeligibilityrequests",
        ),
    ),
    path(
        "api/",
        include("dfhir.contracts.urls", namespace="contracts"),
    ),
    path(
        "api/",
        include(
            "dfhir.biologicallyderivedproducts.urls",
            namespace="biologicallyderivedproducts",
        ),
    ),
    path(
        "api/",
        include("dfhir.enrollmentresponses.urls", namespace="enrollmentresponses"),
    ),
    path(
        "api/",
        include("dfhir.nutritionproducts.urls", namespace="nutritionproducts"),
    ),
    path(
        "api/",
        include("dfhir.allergyintolerances.urls", namespace="allergyintolerances"),
    ),
    path(
        "api/",
        include("dfhir.specimendefinitions.urls", namespace="specimendefinitions"),
    ),
    path(
        "api/",
        include(
            "dfhir.coverageeligibilityresponses.urls",
            namespace="coverageeligibilityresponses",
        ),
    ),
    path(
        "api/",
        include("dfhir.accounts.urls", namespace="accounts"),
    ),
    path(
        "api/",
        include("dfhir.appointmentresponses.urls", namespace="appointmentresponses"),
    ),
    path(
        "api/",
        include("dfhir.detectedissues.urls", namespace="detectedissues"),
    ),
    path("api/", include("dfhir.riskassessments.urls", namespace="riskassessments")),
    path(
        "api/",
        include("dfhir.familymemberhistories.urls", namespace="familymemberhistories"),
    ),
    path(
        "api/",
        include("dfhir.careplans.urls", namespace="careplans"),
    ),
    path(
        "api/",
        include("dfhir.goals.urls", namespace="goals"),
    ),
    path("api/", include("dfhir.nutritionintakes.urls", namespace="nutritionintakse")),
    path(
        "api/",
        include("dfhir.nutritionorders.urls", namespace="nutritionorders"),
    ),
    path(
        "api/",
        include("dfhir.coverages.urls", namespace="coverages"),
    ),
    path("api/", include("dfhir.conditions.urls", namespace="conditions")),
    path(
        "api/",
        include("dfhir.adverseevents.urls", namespace="adverseevents"),
    ),
    path("api/", include("dfhir.bodystructures.urls", namespace="bodystructures")),
    path("api/", include("dfhir.specimens.urls", namespace="specimens")),
    path(
        "api/",
        include("dfhir.documentreferences.urls", namespace="documentreferences"),
    ),
    path(
        "api/",
        include(
            "dfhir.paymentreconciliations.urls", namespace="paymentreconciliations"
        ),
    ),
    path(
        "api/",
        include("dfhir.medicationknowledges.urls", namespace="medicationknowledges"),
    ),
    path("api/", include("dfhir.genomicstudy.urls", namespace="genomicstudy")),
    path(
        "api/",
        include(
            "dfhir.immunizationrecommendations.urls",
            namespace="immunizationrecommendations",
        ),
    ),
    path(
        "api/",
        include("dfhir.claims.urls", namespace="claims"),
    ),
    path(
        "api/",
        include("dfhir.invoices.urls", namespace="invoices"),
    ),
    path("api/", include("dfhir.chargeitems.urls", namespace="chargeitems")),
    path(
        "api/",
        include("dfhir.molecularsequences.urls", namespace="molecularsequences"),
    ),
    path("api/", include("dfhir.imagingstudy.urls", namespace="imagingstudy")),
    path(
        "api/",
        include("dfhir.medicationstatements.urls", namespace="medicationstatements"),
    ),
    path(
        "api/",
        include(
            "dfhir.immunizationevaluations.urls", namespace="immunizationevaluations"
        ),
    ),
    path("api/", include("dfhir.formularyitems.urls", namespace="formularyitems")),
    path("api/", include("dfhir.immunizations.urls", namespace="immunizations")),
    path(
        "api/", include("dfhir.imagingselections.urls", namespace="imagingselections")
    ),
    path(
        "api/",
        include("dfhir.moleculardefinitions.urls", namespace="moleculardefinitions"),
    ),
    path(
        "api/",
        include("dfhir.explanationofbenefits.urls", namespace="explanationofbenefits"),
    ),
    path("api/", include("dfhir.inventoryreports.urls", namespace="inventoryreports")),
    path("api/", include("dfhir.supplyrequests.urls", namespace="supplyrequests")),
    path(
        "api/",
        include("dfhir.deviceassociations.urls", namespace="deviceassociations"),
    ),
    path("api/", include("dfhir.tasks.urls", namespace="tasks")),
    path("api/", include("dfhir.supplydelivery.urls", namespace="supplydelivery")),
    path("api/", include("dfhir.transports.urls", namespace="transports")),
    path(
        "api/",
        include("dfhir.deviceusages.urls", namespace="deviceusages"),
    ),
    path(
        "api/",
        include("dfhir.claimresponses.urls", namespace="claimresponses"),
    ),
    path(
        "api/",
        include("dfhir.plandefinitions.urls", namespace="plandefinitions"),
    ),
    path(
        "api/",
        include("dfhir.devicerequests.urls", namespace="devicerequests"),
    ),
    path(
        "api/",
        include("dfhir.activitydefinitions.urls", namespace="activitydefinitions"),
    ),
    path(
        "api/",
        include(
            "dfhir.biologicallyderivedproductdispenses.urls",
            namespace="biologicallyderivedproductdispenses",
        ),
    ),
    path(
        "api/", include("dfhir.practitionerroles.urls", namespace="practitionerroles")
    ),
    # path("api/", include("dfhir.provenances.urls", namespace="provenance")),
    path("api/", include("dfhir.provenances.urls", namespace="provenance")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

# API URLS
urlpatterns += [
    # API base url
    # path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    # path(
    #     "api/docs/",
    #     SpectacularSwaggerView.as_view(url_name="api-schema"),
    #     name="api-docs",
    # ),
]
