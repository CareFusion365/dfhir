"""base models test."""

from datetime import datetime

from django.test import TestCase
from django.utils import timezone

from dfhir.base.choices import (
    AddressTypeChoices,
    AddressUseChoices,
    ContactPointSystemChoices,
    ContactPointUseChoices,
    HumanNameUseChoices,
    MonetaryComponentChoices,
    QuantityComparatorChoices,
    RelatedArtifactTypeChoices,
    RepeatDurationUnits,
    TriggerDefinitionTypeChoices,
)
from dfhir.base.models import (
    Address,
    Age,
    Annotation,
    Attachment,
    Availability,
    AvailableTime,
    CodeableConcept,
    CodeableReference,
    Coding,
    Communication,
    ConnectionType,
    ContactDetail,
    ContactPoint,
    Duration,
    Expression,
    ExtendedContactDetail,
    HumanName,
    Identifier,
    MonetaryComponent,
    Money,
    NotAvailableTime,
    OrganizationReference,
    Payload,
    Period,
    ProductShelfLife,
    Qualification,
    Quantity,
    Range,
    Ratio,
    Reference,
    RelatedArtifact,
    RelativeTime,
    Repeat,
    ServiceType,
    Signature,
    SignatureOnBehalfOfReference,
    SignatureWhoReference,
    SimpleQuantity,
    Timing,
    TriggerDefinition,
    UsageContext,
    VirtualServiceDetailAddress,
    VirtualServiceDetails,
)


class TestPeriod(TestCase):
    """test period model."""

    def setUp(self):
        """Period test setup."""
        self.period = Period.objects.create(
            start=timezone.make_aware(datetime(2021, 1, 1)),
            end=timezone.make_aware(datetime(2021, 1, 31)),
        )

    def test_period_create(self):
        """Test period create."""
        self.assertEqual(self.period.start, timezone.make_aware(datetime(2021, 1, 1)))
        self.assertEqual(self.period.end, timezone.make_aware(datetime(2021, 1, 31)))

    def test_period_update(self):
        """Test period update."""
        self.period.start = timezone.make_aware(datetime(2021, 2, 1))
        self.period.save()
        self.assertEqual(self.period.start, timezone.make_aware(datetime(2021, 2, 1)))

    def test_period_delete(self):
        """Test period delete."""
        self.period.delete()
        self.assertFalse(Period.objects.exists())


class TestServiceType(TestCase):
    """test service type model."""

    def setUp(self):
        """Service type test setup."""
        self.service_type = ServiceType.objects.create(
            display="test service type", description="test service type description"
        )

    def test_service_type_create(self):
        """Test service type create."""
        self.assertEqual(self.service_type.display, "test service type")
        self.assertEqual(self.service_type.description, "test service type description")

    def test_service_type_update(self):
        """Test service type update."""
        self.service_type.display = "updated service type"
        self.service_type.save()
        self.assertEqual(self.service_type.display, "updated service type")

    def test_service_type_delete(self):
        """Test service type delete."""
        self.service_type.delete()
        self.assertFalse(ServiceType.objects.exists())


class TestContactPoint(TestCase):
    """test contact point model."""

    def setUp(self):
        """Contact point test setup."""
        self.period = Period.objects.create(
            start=timezone.make_aware(datetime(2021, 1, 1)),
            end=timezone.make_aware(datetime(2021, 1, 31)),
        )
        self.contact_point = ContactPoint.objects.create(
            system=ContactPointSystemChoices.EMAIL,
            value="Contact Point Value",
            use=ContactPointUseChoices.WORK,
            rank=1,
        )

    def test_contact_point_create(self):
        """Test contact point create."""
        self.assertEqual(self.contact_point.system, ContactPointSystemChoices.EMAIL)
        self.assertEqual(self.contact_point.value, "Contact Point Value")
        self.assertEqual(self.contact_point.use, ContactPointUseChoices.WORK)
        self.assertEqual(self.contact_point.rank, 1)

    def test_contact_point_update(self):
        """Test contact point update."""
        self.contact_point.value = "Updated Contact Point Value"
        self.contact_point.save()
        self.assertEqual(self.contact_point.value, "Updated Contact Point Value")


class TestAddress(TestCase):
    """test address model."""

    def setUp(self):
        """Address test setup."""
        self.period = Period.objects.create(
            start=timezone.make_aware(datetime(2021, 1, 1, 0, 0, 0)),
            end=timezone.make_aware(datetime(2021, 1, 31, 23, 59, 59)),
        )
        self.address = Address.objects.create(
            use=AddressUseChoices.HOME,
            type=AddressTypeChoices.PHYSICAL,
            text="Address Text",
            line=["Address Line 1", "Address Line 2"],
            city="Address City",
            state="Address State",
            postal_code="Address Postal Code",
            country="Address Country",
            period=self.period,
        )

    def test_address_create(self):
        """Test address create."""
        self.assertEqual(self.address.use, AddressUseChoices.HOME)
        self.assertEqual(self.address.type, AddressTypeChoices.PHYSICAL)
        self.assertEqual(self.address.text, "Address Text")
        self.assertEqual(self.address.line, ["Address Line 1", "Address Line 2"])
        self.assertEqual(self.address.city, "Address City")
        self.assertEqual(self.address.state, "Address State")
        self.assertEqual(self.address.postal_code, "Address Postal Code")
        self.assertEqual(self.address.country, "Address Country")

    def test_address_update(self):
        """Test address update."""
        self.address.city = "Updated Address City"
        self.address.period = None
        self.address.type = AddressTypeChoices.BOTH
        self.address.line = ["Updated Address Line 1", "Updated Address Line 2"]

        self.address.save()
        self.assertEqual(self.address.city, "Updated Address City")
        self.assertEqual(self.address.type, AddressTypeChoices.BOTH)
        self.assertEqual(
            self.address.line, ["Updated Address Line 1", "Updated Address Line 2"]
        )
        self.assertIsNone(self.address.period)


class ContactDetailTest(TestCase):
    """test contact detail model."""

    def setUp(self):
        """Contact detail test setup."""
        self.telecom = ContactPoint.objects.create()
        self.contact_detail = ContactDetail.objects.create(name="Contact Detail Name")
        self.contact_detail.telecom.add(self.telecom)

    def test_contact_detail_create(self):
        """Test contact detail create."""
        self.assertEqual(self.contact_detail.name, "Contact Detail Name")
        self.assertTrue(self.contact_detail.telecom.filter(id=self.telecom.id).exists())

    def test_contact_detail_update(self):
        """Test contact detail update."""
        self.contact_detail.name = "Updated Contact Detail Name"
        self.contact_detail.save()
        self.assertEqual(self.contact_detail.name, "Updated Contact Detail " "Name")

    def test_delete_contact_detail(self):
        """Test contact detail delete."""
        self.contact_detail.delete()
        self.assertFalse(ContactDetail.objects.exists())


class TestAvailableTime(TestCase):
    """test available time model."""

    def setUp(self):
        """Available time test setup."""
        self.available_time = AvailableTime.objects.create(
            days_of_week=["Monday", "Tuesday"],
            all_day=True,
            available_start_time="09:00:00",
            available_end_time="17:00:00",
        )

    def test_available_time_create(self):
        """Test available time create."""
        self.assertEqual(self.available_time.days_of_week, ["Monday", "Tuesday"])
        self.assertTrue(self.available_time.all_day)
        self.assertEqual(self.available_time.available_start_time, "09:00:00")
        self.assertEqual(self.available_time.available_end_time, "17:00:00")

    def test_available_time_update(self):
        """Test available time update."""
        self.available_time.days_of_week = ["Wednesday", "Thursday"]
        self.available_time.save()
        self.assertEqual(self.available_time.days_of_week, ["Wednesday", "Thursday"])

    def test_delete_available_time(self):
        """Test available time delete."""
        self.available_time.delete()
        self.assertFalse(AvailableTime.objects.exists())


class TestNotAvailableTime(TestCase):
    """test not available time model."""

    def setUp(self):
        """Not available time test setup."""
        self.period = Period.objects.create(
            start=timezone.make_aware(datetime(2021, 1, 1)),
            end=timezone.make_aware(datetime(2021, 1, 31)),
        )
        self.not_available_time = NotAvailableTime.objects.create(
            description="Test Not Available Time Description",
            during=self.period,
        )

    def test_create_not_available_time(self):
        """Test create available time."""
        self.assertEqual(
            self.not_available_time.description, "Test Not Available Time Description"
        )
        self.assertEqual(self.not_available_time.during, self.period)


class TestAvailability(TestCase):
    """test availability model."""

    def setUp(self):
        """Availability test setup."""
        self.period = Period.objects.create(
            start=timezone.make_aware(datetime(2021, 1, 1)),
            end=timezone.make_aware(datetime(2021, 1, 31)),
        )
        self.available_time = AvailableTime.objects.create(
            days_of_week=["Monday", "Tuesday"],
            all_day=True,
            available_start_time="09:00:00",
            available_end_time="17:00:00",
        )
        self.not_available_time = NotAvailableTime.objects.create(
            description="Test Not Available Time Description",
            during=self.period,
        )
        self.availability = Availability.objects.create(period=self.period)
        self.availability.available_time.add(self.available_time)
        self.availability.not_available_time.add(self.not_available_time)

    def test_availability_create(self):
        """Test availability create."""
        self.assertEqual(self.availability.period, self.period)
        assert self.available_time in self.availability.available_time.all()
        assert self.not_available_time in self.availability.not_available_time.all()

    def test_availability_update(self):
        """Test availability update."""
        self.availability.period = None
        self.availability.save()
        self.assertIsNone(self.availability.period)

    def test_delete_availability(self):
        """Test availability delete."""
        self.availability.delete()
        self.assertFalse(Availability.objects.exists())


class TestReference(TestCase):
    """test reference model."""

    def setUp(self):
        """Reference test setup."""
        self.reference = Reference.objects.create(
            reference="Reference",
            type="Type",
            display="Display",
        )

    def test_reference_create(self):
        """Test reference create."""
        self.assertEqual(self.reference.reference, "Reference")
        self.assertEqual(self.reference.type, "Type")
        self.assertEqual(self.reference.display, "Display")

    def test_reference_update(self):
        """Test reference update."""
        self.reference.display = "Updated Display"
        self.reference.save()
        self.assertEqual(self.reference.display, "Updated Display")

    def test_reference_delete(self):
        """Test reference delete."""
        self.reference.delete()
        self.assertFalse(Reference.objects.exists())


class TestHumanName(TestCase):
    """test human name model."""

    def setUp(self):
        """Human name test setup."""
        self.period = Period.objects.create(
            start=timezone.make_aware(datetime(2021, 1, 1)),
            end=timezone.make_aware(datetime(2021, 1, 31)),
        )
        self.human_name = HumanName.objects.create(
            use=HumanNameUseChoices.USUAL,
            text="Human Name Text",
            family="Family Name",
            given=["Given Name 1", "Given Name 2"],
            prefix=["Prefix 1"],
            suffix=["Suffix 1"],
            period=self.period,
        )

    def test_human_name_create(self):
        """Test human name create."""
        self.assertEqual(self.human_name.use, HumanNameUseChoices.USUAL)
        self.assertEqual(self.human_name.text, "Human Name Text")
        self.assertEqual(self.human_name.family, "Family Name")
        self.assertEqual(self.human_name.given, ["Given Name 1", "Given Name 2"])
        self.assertEqual(self.human_name.period, self.period)

    def test_human_name_update(self):
        """Test human name update."""
        self.human_name.family = "Updated Family Name"
        self.human_name.save()
        self.assertEqual(self.human_name.family, "Updated Family Name")

    def test_human_name_delete(self):
        """Test human name delete."""
        self.human_name.delete()
        self.assertFalse(HumanName.objects.exists())


class TestExtendedContactDetail(TestCase):
    """test extended contact detail model."""

    def setUp(self):
        """Extended contact detail test setup."""
        self.extended_contact_detail = ExtendedContactDetail.objects.create(
            purpose=CodeableConcept.objects.create(text="Purpose"),
            address=Address.objects.create(text="Address"),
        )
        self.extended_contact_detail.name.add(HumanName.objects.create(text="Name"))

    def test_extended_contact_detail_create(self):
        """Test extended contact detail create."""
        self.assertEqual(self.extended_contact_detail.purpose.text, "Purpose")
        self.assertTrue(self.extended_contact_detail.name.filter(text="Name").exists())
        self.assertEqual(self.extended_contact_detail.address.text, "Address")

    def test_extended_contact_detail_update(self):
        """Test extended contact detail update."""
        self.extended_contact_detail.address.text = "Updated Address"
        self.extended_contact_detail.address.save()
        self.assertEqual(self.extended_contact_detail.address.text, "Updated Address")

    def test_extended_contact_detail_delete(self):
        """Test extended contact detail delete."""
        self.extended_contact_detail.delete()
        self.assertFalse(ExtendedContactDetail.objects.exists())


class TestAttachment(TestCase):
    """test attachment model."""

    def setUp(self):
        """Attachment test setup."""
        self.attachment = Attachment.objects.create(
            title="Title",
            content_type="text/plain",
            language="en",
            data="RGF0YQ==",
            url="https://example.com",
            size=4,
        )

    def test_attachment_create(self):
        """Test attachment create."""
        self.assertEqual(self.attachment.title, "Title")
        self.assertEqual(self.attachment.content_type, "text/plain")
        self.assertEqual(self.attachment.size, 4)

    def test_attachment_update(self):
        """Test attachment update."""
        self.attachment.title = "Updated Title"
        self.attachment.save()
        self.assertEqual(self.attachment.title, "Updated Title")

    def test_attachment_delete(self):
        """Test attachment delete."""
        self.attachment.delete()
        self.assertFalse(Attachment.objects.exists())


class TestCoding(TestCase):
    """test coding model."""

    def setUp(self):
        """Coding test setup."""
        self.coding = Coding.objects.create(
            system="System",
            version="1.0",
            code="Code",
            display="Display",
            user_selected=True,
        )

    def test_coding_create(self):
        """Test coding create."""
        self.assertEqual(self.coding.system, "System")
        self.assertEqual(self.coding.code, "Code")
        self.assertTrue(self.coding.user_selected)

    def test_coding_update(self):
        """Test coding update."""
        self.coding.display = "Updated Display"
        self.coding.save()
        self.assertEqual(self.coding.display, "Updated Display")

    def test_coding_delete(self):
        """Test coding delete."""
        self.coding.delete()
        self.assertFalse(Coding.objects.exists())


class TestCodeableConcept(TestCase):
    """test codeable concept model."""

    def setUp(self):
        """Codeable concept test setup."""
        self.coding = Coding.objects.create(display="Coding")
        self.codeable_concept = CodeableConcept.objects.create(text="Text")
        self.codeable_concept.coding.add(self.coding)

    def test_codeable_concept_create(self):
        """Test codeable concept create."""
        self.assertEqual(self.codeable_concept.text, "Text")
        assert self.coding in self.codeable_concept.coding.all()

    def test_codeable_concept_update(self):
        """Test codeable concept update."""
        self.codeable_concept.text = "Updated Text"
        self.codeable_concept.save()
        self.assertEqual(self.codeable_concept.text, "Updated Text")

    def test_codeable_concept_delete(self):
        """Test codeable concept delete."""
        self.codeable_concept.delete()
        self.assertFalse(CodeableConcept.objects.exists())


class TestOrganizationReference(TestCase):
    """test organization reference model."""

    def setUp(self):
        """Organization reference test setup."""
        self.organization_reference = OrganizationReference.objects.create(
            display="Organization Display"
        )

    def test_organization_reference_create(self):
        """Test organization reference create."""
        self.assertEqual(self.organization_reference.display, "Organization Display")

    def test_organization_reference_update(self):
        """Test organization reference update."""
        self.organization_reference.display = "Updated Organization Display"
        self.organization_reference.save()
        self.assertEqual(
            self.organization_reference.display, "Updated Organization Display"
        )

    def test_organization_reference_delete(self):
        """Test organization reference delete."""
        self.organization_reference.delete()
        self.assertFalse(OrganizationReference.objects.exists())


class TestIdentifier(TestCase):
    """test identifier model."""

    def setUp(self):
        """Identifier test setup."""
        self.identifier = Identifier.objects.create(
            use="usual",
            system="System",
            value="Value",
        )

    def test_identifier_create(self):
        """Test identifier create."""
        self.assertEqual(self.identifier.use, "usual")
        self.assertEqual(self.identifier.value, "Value")

    def test_identifier_update(self):
        """Test identifier update."""
        self.identifier.value = "Updated Value"
        self.identifier.save()
        self.assertEqual(self.identifier.value, "Updated Value")

    def test_identifier_delete(self):
        """Test identifier delete."""
        self.identifier.delete()
        self.assertFalse(Identifier.objects.exists())


class TestQualification(TestCase):
    """test qualification model."""

    def setUp(self):
        """Qualification test setup."""
        self.qualification = Qualification.objects.create(
            code=CodeableConcept.objects.create(text="Qualification Code")
        )

    def test_qualification_create(self):
        """Test qualification create."""
        self.assertEqual(self.qualification.code.text, "Qualification Code")

    def test_qualification_update(self):
        """Test qualification update."""
        self.qualification.code.text = "Updated Qualification Code"
        self.qualification.code.save()
        self.assertEqual(self.qualification.code.text, "Updated Qualification Code")

    def test_qualification_delete(self):
        """Test qualification delete."""
        self.qualification.delete()
        self.assertFalse(Qualification.objects.exists())


class TestConnectionType(TestCase):
    """test connection type model."""

    def setUp(self):
        """Connection type test setup."""
        self.connection_type = ConnectionType.objects.create(
            display="Connection Type Display"
        )

    def test_connection_type_create(self):
        """Test connection type create."""
        self.assertEqual(self.connection_type.display, "Connection Type Display")

    def test_connection_type_update(self):
        """Test connection type update."""
        self.connection_type.display = "Updated Connection Type Display"
        self.connection_type.save()
        self.assertEqual(
            self.connection_type.display, "Updated Connection Type Display"
        )

    def test_connection_type_delete(self):
        """Test connection type delete."""
        self.connection_type.delete()
        self.assertFalse(ConnectionType.objects.exists())


class TestPayload(TestCase):
    """test payload model."""

    def setUp(self):
        """Payload test setup."""
        self.payload = Payload.objects.create(
            profile_uri=["https://example.com/profile"],
        )
        self.codeable_concept = CodeableConcept.objects.create(text="Payload Type")
        self.payload.type.add(self.codeable_concept)

    def test_payload_create(self):
        """Test payload create."""
        assert self.codeable_concept in self.payload.type.all()
        self.assertEqual(self.payload.profile_uri, ["https://example.com/profile"])

    def test_payload_update(self):
        """Test payload update."""
        self.payload.profile_uri = ["https://example.com/updated_profile"]
        self.payload.save()
        self.assertEqual(
            self.payload.profile_uri, ["https://example.com/updated_profile"]
        )

    def test_payload_delete(self):
        """Test payload delete."""
        self.payload.delete()
        self.assertFalse(Payload.objects.exists())


class TestVirtualServiceDetailAddress(TestCase):
    """test virtual service detail address model."""

    def setUp(self):
        """Virtual service detail address test setup."""
        self.virtual_service_detail_address = (
            VirtualServiceDetailAddress.objects.create(
                address_string="Virtual Address",
                address_url="https://example.com/virtual",
            )
        )

    def test_virtual_service_detail_address_create(self):
        """Test virtual service detail address create."""
        self.assertEqual(
            self.virtual_service_detail_address.address_string, "Virtual Address"
        )
        self.assertEqual(
            self.virtual_service_detail_address.address_url,
            "https://example.com/virtual",
        )

    def test_virtual_service_detail_address_update(self):
        """Test virtual service detail address update."""
        self.virtual_service_detail_address.address_string = "Updated Virtual Address"
        self.virtual_service_detail_address.save()
        self.assertEqual(
            self.virtual_service_detail_address.address_string,
            "Updated Virtual Address",
        )

    def test_virtual_service_detail_address_delete(self):
        """Test virtual service detail address delete."""
        self.virtual_service_detail_address.delete()
        self.assertFalse(VirtualServiceDetailAddress.objects.exists())


class TestVirtualServiceDetails(TestCase):
    """test virtual service details model."""

    def setUp(self):
        """Virtual service details test setup."""
        self.virtual_service_details = VirtualServiceDetails.objects.create(
            channel_type=Coding.objects.create(display="Channel Type"),
            session_key="Session Key",
        )

    def test_virtual_service_details_create(self):
        """Test virtual service details create."""
        self.assertEqual(
            self.virtual_service_details.channel_type.display, "Channel Type"
        )
        self.assertEqual(self.virtual_service_details.session_key, "Session Key")

    def test_virtual_service_details_update(self):
        """Test virtual service details update."""
        self.virtual_service_details.session_key = "Updated Session Key"
        self.virtual_service_details.save()
        self.assertEqual(
            self.virtual_service_details.session_key, "Updated Session Key"
        )

    def test_virtual_service_details_delete(self):
        """Test virtual service details delete."""
        self.virtual_service_details.delete()
        self.assertFalse(VirtualServiceDetails.objects.exists())


class TestQuantity(TestCase):
    """test quantity model."""

    def setUp(self):
        """Quantity test setup."""
        self.quantity = Quantity.objects.create(
            value=10.5,
            comparator=QuantityComparatorChoices.GREATER_THAN,
            unit="mg",
        )

    def test_quantity_create(self):
        """Test quantity create."""
        self.assertEqual(self.quantity.value, 10.5)
        self.assertEqual(
            self.quantity.comparator, QuantityComparatorChoices.GREATER_THAN
        )

    def test_quantity_update(self):
        """Test quantity update."""
        self.quantity.value = 20.0
        self.quantity.save()
        self.assertEqual(self.quantity.value, 20.0)

    def test_quantity_delete(self):
        """Test quantity delete."""
        self.quantity.delete()
        self.assertFalse(Quantity.objects.exists())


class TestRange(TestCase):
    """test range model."""

    def setUp(self):
        """Range test setup."""
        self.range = Range.objects.create(
            low=Quantity.objects.create(value=1.0),
            high=Quantity.objects.create(value=10.0),
        )

    def test_range_create(self):
        """Test range create."""
        self.assertEqual(self.range.low.value, 1.0)
        self.assertEqual(self.range.high.value, 10.0)

    def test_range_update(self):
        """Test range update."""
        self.range.low.value = 2.0
        self.range.low.save()
        self.assertEqual(self.range.low.value, 2.0)

    def test_range_delete(self):
        """Test range delete."""
        self.range.delete()
        self.assertFalse(Range.objects.exists())


class TestAnnotation(TestCase):
    """test annotation model."""

    def setUp(self):
        """Annotation test setup."""
        self.annotation = Annotation.objects.create(
            text="Annotation Text",
            time=timezone.now(),
        )

    def test_annotation_create(self):
        """Test annotation create."""
        self.assertEqual(self.annotation.text, "Annotation Text")

    def test_annotation_update(self):
        """Test annotation update."""
        self.annotation.text = "Updated Annotation Text"
        self.annotation.save()
        self.assertEqual(self.annotation.text, "Updated Annotation Text")

    def test_annotation_delete(self):
        """Test annotation delete."""
        self.annotation.delete()
        self.assertFalse(Annotation.objects.exists())


class TestCommunication(TestCase):
    """test communication model."""

    def setUp(self):
        """Communication test setup."""
        self.communication = Communication.objects.create(
            language=CodeableConcept.objects.create(text="Language"),
            preferred=True,
        )

    def test_communication_create(self):
        """Test communication create."""
        self.assertEqual(self.communication.language.text, "Language")
        self.assertTrue(self.communication.preferred)

    def test_communication_update(self):
        """Test communication update."""
        self.communication.preferred = False
        self.communication.save()
        self.assertFalse(self.communication.preferred)

    def test_communication_delete(self):
        """Test communication delete."""
        self.communication.delete()
        self.assertFalse(Communication.objects.exists())


class TestRatio(TestCase):
    """test ratio model."""

    def setUp(self):
        """Ratio test setup."""
        self.ratio = Ratio.objects.create(
            numerator=Quantity.objects.create(value=1.0),
            denominator=Quantity.objects.create(value=2.0),
        )

    def test_ratio_create(self):
        """Test ratio create."""
        self.assertEqual(self.ratio.numerator.value, 1.0)
        self.assertEqual(self.ratio.denominator.value, 2.0)

    def test_ratio_update(self):
        """Test ratio update."""
        self.ratio.numerator.value = 3.0
        self.ratio.numerator.save()
        self.assertEqual(self.ratio.numerator.value, 3.0)

    def test_ratio_delete(self):
        """Test ratio delete."""
        self.ratio.delete()
        self.assertFalse(Ratio.objects.exists())


class TestCodeableReference(TestCase):
    """test codeable reference model."""

    def setUp(self):
        """Codeable reference test setup."""
        self.codeable_reference = CodeableReference.objects.create(
            concept=CodeableConcept.objects.create(text="Concept")
        )

    def test_codeable_reference_create(self):
        """Test codeable reference create."""
        self.assertEqual(self.codeable_reference.concept.text, "Concept")

    def test_codeable_reference_update(self):
        """Test codeable reference update."""
        self.codeable_reference.concept.text = "Updated Concept"
        self.codeable_reference.concept.save()
        self.assertEqual(self.codeable_reference.concept.text, "Updated Concept")

    def test_codeable_reference_delete(self):
        """Test codeable reference delete."""
        self.codeable_reference.delete()
        self.assertFalse(CodeableReference.objects.exists())


class TestRepeat(TestCase):
    """test repeat model."""

    def setUp(self):
        """Repeat test setup."""
        self.repeat = Repeat.objects.create(
            count=1,
            duration=1.0,
            duration_unit=RepeatDurationUnits.DAY,
        )

    def test_repeat_create(self):
        """Test repeat create."""
        self.assertEqual(self.repeat.count, 1)
        self.assertEqual(self.repeat.duration_unit, RepeatDurationUnits.DAY)

    def test_repeat_update(self):
        """Test repeat update."""
        self.repeat.count = 2
        self.repeat.save()
        self.assertEqual(self.repeat.count, 2)

    def test_repeat_delete(self):
        """Test repeat delete."""
        self.repeat.delete()
        self.assertFalse(Repeat.objects.exists())


class TestTiming(TestCase):
    """test timing model."""

    def setUp(self):
        """Timing test setup."""
        self.timing = Timing.objects.create(
            repeat=Repeat.objects.create(count=1),
            code=CodeableConcept.objects.create(text="Timing Code"),
        )

    def test_timing_create(self):
        """Test timing create."""
        self.assertEqual(self.timing.repeat.count, 1)
        self.assertEqual(self.timing.code.text, "Timing Code")

    def test_timing_update(self):
        """Test timing update."""
        self.timing.code.text = "Updated Timing Code"
        self.timing.code.save()
        self.assertEqual(self.timing.code.text, "Updated Timing Code")

    def test_timing_delete(self):
        """Test timing delete."""
        self.timing.delete()
        self.assertFalse(Timing.objects.exists())


class TestRelatedArtifact(TestCase):
    """test related artifact model."""

    def setUp(self):
        """Related artifact test setup."""
        self.related_artifact = RelatedArtifact.objects.create(
            type=RelatedArtifactTypeChoices.DOCUMENTATION,
            label="Label",
            display="Display",
        )

    def test_related_artifact_create(self):
        """Test related artifact create."""
        self.assertEqual(
            self.related_artifact.type, RelatedArtifactTypeChoices.DOCUMENTATION
        )
        self.assertEqual(self.related_artifact.label, "Label")

    def test_related_artifact_update(self):
        """Test related artifact update."""
        self.related_artifact.label = "Updated Label"
        self.related_artifact.save()
        self.assertEqual(self.related_artifact.label, "Updated Label")

    def test_related_artifact_delete(self):
        """Test related artifact delete."""
        self.related_artifact.delete()
        self.assertFalse(RelatedArtifact.objects.exists())


class TestUsageContext(TestCase):
    """test usage context model."""

    def setUp(self):
        """Usage context test setup."""
        self.usage_context = UsageContext.objects.create(
            code=Coding.objects.create(display="Usage Code"),
            value_codeable_concept=CodeableConcept.objects.create(text="Value Concept"),
        )

    def test_usage_context_create(self):
        """Test usage context create."""
        self.assertEqual(self.usage_context.code.display, "Usage Code")
        self.assertEqual(
            self.usage_context.value_codeable_concept.text, "Value Concept"
        )

    def test_usage_context_update(self):
        """Test usage context update."""
        self.usage_context.value_codeable_concept.text = "Updated Value Concept"
        self.usage_context.value_codeable_concept.save()
        self.assertEqual(
            self.usage_context.value_codeable_concept.text, "Updated Value Concept"
        )

    def test_usage_context_delete(self):
        """Test usage context delete."""
        self.usage_context.delete()
        self.assertFalse(UsageContext.objects.exists())


class TestProductShelfLife(TestCase):
    """test product shelf life model."""

    def setUp(self):
        """Product shelf life test setup."""
        self.product_shelf_life = ProductShelfLife.objects.create(
            type=CodeableConcept.objects.create(text="Shelf Life Type"),
            period_duration=Duration.objects.create(value=1.0),
        )

    def test_product_shelf_life_create(self):
        """Test product shelf life create."""
        self.assertEqual(self.product_shelf_life.type.text, "Shelf Life Type")
        self.assertEqual(self.product_shelf_life.period_duration.value, 1.0)

    def test_product_shelf_life_update(self):
        """Test product shelf life update."""
        self.product_shelf_life.type.text = "Updated Shelf Life Type"
        self.product_shelf_life.type.save()
        self.assertEqual(self.product_shelf_life.type.text, "Updated Shelf Life Type")

    def test_product_shelf_life_delete(self):
        """Test product shelf life delete."""
        self.product_shelf_life.delete()
        self.assertFalse(ProductShelfLife.objects.exists())


class TestExpression(TestCase):
    """test expression model."""

    def setUp(self):
        """Expression test setup."""
        self.expression = Expression.objects.create(
            description="Expression Description",
            name="Expression Name",
            language="text/cql",
            expression="today()",
        )

    def test_expression_create(self):
        """Test expression create."""
        self.assertEqual(self.expression.name, "Expression Name")
        self.assertEqual(self.expression.expression, "today()")

    def test_expression_update(self):
        """Test expression update."""
        self.expression.name = "Updated Expression Name"
        self.expression.save()
        self.assertEqual(self.expression.name, "Updated Expression Name")

    def test_expression_delete(self):
        """Test expression delete."""
        self.expression.delete()
        self.assertFalse(Expression.objects.exists())


class TestRelativeTime(TestCase):
    """test relative time model."""

    def setUp(self):
        """Relative time test setup."""
        self.relative_time = RelativeTime.objects.create(
            context_path="Context Path",
            offset_duration=Quantity.objects.create(value=1.0),
        )

    def test_relative_time_create(self):
        """Test relative time create."""
        self.assertEqual(self.relative_time.context_path, "Context Path")
        self.assertEqual(self.relative_time.offset_duration.value, 1.0)

    def test_relative_time_update(self):
        """Test relative time update."""
        self.relative_time.context_path = "Updated Context Path"
        self.relative_time.save()
        self.assertEqual(self.relative_time.context_path, "Updated Context Path")

    def test_relative_time_delete(self):
        """Test relative time delete."""
        self.relative_time.delete()
        self.assertFalse(RelativeTime.objects.exists())


class TestAge(TestCase):
    """test age model."""

    def setUp(self):
        """Age test setup."""
        self.age = Age.objects.create(value=25.0, unit="years")

    def test_age_create(self):
        """Test age create."""
        self.assertEqual(self.age.value, 25.0)
        self.assertEqual(self.age.unit, "years")

    def test_age_update(self):
        """Test age update."""
        self.age.value = 26.0
        self.age.save()
        self.assertEqual(self.age.value, 26.0)

    def test_age_delete(self):
        """Test age delete."""
        self.age.delete()
        self.assertFalse(Age.objects.exists())


class TestDuration(TestCase):
    """test duration model."""

    def setUp(self):
        """Duration test setup."""
        self.duration = Duration.objects.create(value=60.0, unit="seconds")

    def test_duration_create(self):
        """Test duration create."""
        self.assertEqual(self.duration.value, 60.0)
        self.assertEqual(self.duration.unit, "seconds")

    def test_duration_update(self):
        """Test duration update."""
        self.duration.value = 120.0
        self.duration.save()
        self.assertEqual(self.duration.value, 120.0)

    def test_duration_delete(self):
        """Test duration delete."""
        self.duration.delete()
        self.assertFalse(Duration.objects.exists())


class TestSimpleQuantity(TestCase):
    """test simple quantity model."""

    def setUp(self):
        """Simple quantity test setup."""
        self.simple_quantity = SimpleQuantity.objects.create(value=1.0, unit="unit")

    def test_simple_quantity_create(self):
        """Test simple quantity create."""
        self.assertEqual(self.simple_quantity.value, 1.0)

    def test_simple_quantity_update(self):
        """Test simple quantity update."""
        self.simple_quantity.value = 2.0
        self.simple_quantity.save()
        self.assertEqual(self.simple_quantity.value, 2.0)

    def test_simple_quantity_delete(self):
        """Test simple quantity delete."""
        self.simple_quantity.delete()
        self.assertFalse(SimpleQuantity.objects.exists())


class TestMoney(TestCase):
    """test money model."""

    def setUp(self):
        """Money test setup."""
        self.money = Money.objects.create(value=100.0, currency="USD")

    def test_money_create(self):
        """Test money create."""
        self.assertEqual(self.money.value, 100.0)
        self.assertEqual(self.money.currency, "USD")

    def test_money_update(self):
        """Test money update."""
        self.money.value = 200.0
        self.money.save()
        self.assertEqual(self.money.value, 200.0)

    def test_money_delete(self):
        """Test money delete."""
        self.money.delete()
        self.assertFalse(Money.objects.exists())


class TestMonetaryComponent(TestCase):
    """test monetary component model."""

    def setUp(self):
        """Monetary component test setup."""
        self.monetary_component = MonetaryComponent.objects.create(
            type=MonetaryComponentChoices.BASE,
            code=CodeableConcept.objects.create(text="Monetary Code"),
            amount=Money.objects.create(value=10.0),
        )

    def test_monetary_component_create(self):
        """Test monetary component create."""
        self.assertEqual(self.monetary_component.type, MonetaryComponentChoices.BASE)
        self.assertEqual(self.monetary_component.amount.value, 10.0)

    def test_monetary_component_update(self):
        """Test monetary component update."""
        self.monetary_component.type = MonetaryComponentChoices.TAX
        self.monetary_component.save()
        self.assertEqual(self.monetary_component.type, MonetaryComponentChoices.TAX)

    def test_monetary_component_delete(self):
        """Test monetary component delete."""
        self.monetary_component.delete()
        self.assertFalse(MonetaryComponent.objects.exists())


class TestSignatureWhoReference(TestCase):
    """test signature who reference model."""

    def setUp(self):
        """Signature who reference test setup."""
        self.signature_who_reference = SignatureWhoReference.objects.create(
            display="Who Display"
        )

    def test_signature_who_reference_create(self):
        """Test signature who reference create."""
        self.assertEqual(self.signature_who_reference.display, "Who Display")

    def test_signature_who_reference_update(self):
        """Test signature who reference update."""
        self.signature_who_reference.display = "Updated Who Display"
        self.signature_who_reference.save()
        self.assertEqual(self.signature_who_reference.display, "Updated Who Display")

    def test_signature_who_reference_delete(self):
        """Test signature who reference delete."""
        self.signature_who_reference.delete()
        self.assertFalse(SignatureWhoReference.objects.exists())


class TestSignatureOnBehalfOfReference(TestCase):
    """test signature on behalf of reference model."""

    def setUp(self):
        """Signature on behalf of reference test setup."""
        self.signature_on_behalf_of_reference = (
            SignatureOnBehalfOfReference.objects.create(display="On Behalf Of Display")
        )

    def test_signature_on_behalf_of_reference_create(self):
        """Test signature on behalf of reference create."""
        self.assertEqual(
            self.signature_on_behalf_of_reference.display, "On Behalf Of Display"
        )

    def test_signature_on_behalf_of_reference_update(self):
        """Test signature on behalf of reference update."""
        self.signature_on_behalf_of_reference.display = "Updated On Behalf Of Display"
        self.signature_on_behalf_of_reference.save()
        self.assertEqual(
            self.signature_on_behalf_of_reference.display,
            "Updated On Behalf Of Display",
        )

    def test_signature_on_behalf_of_reference_delete(self):
        """Test signature on behalf of reference delete."""
        self.signature_on_behalf_of_reference.delete()
        self.assertFalse(SignatureOnBehalfOfReference.objects.exists())


class TestSignature(TestCase):
    """test signature model."""

    def setUp(self):
        """Signature test setup."""
        self.signature = Signature.objects.create(
            when=timezone.now(),
            who=SignatureWhoReference.objects.create(display="Who"),
        )
        self.coding = Coding.objects.create(display="Signature Type")
        self.signature.type.add(self.coding)

    def test_signature_create(self):
        """Test signature create."""
        self.assertEqual(self.signature.who.display, "Who")
        assert self.coding in self.signature.type.all()

    def test_signature_update(self):
        """Test signature update."""
        self.signature.who.display = "Updated Who"
        self.signature.who.save()
        self.assertEqual(self.signature.who.display, "Updated Who")

    def test_signature_delete(self):
        """Test signature delete."""
        self.signature.delete()
        self.assertFalse(Signature.objects.exists())


class TestTriggerDefinition(TestCase):
    """test trigger definition model."""

    def setUp(self):
        """Trigger definition test setup."""
        self.trigger_definition = TriggerDefinition.objects.create(
            type=TriggerDefinitionTypeChoices.NAMED_EVENT,
            name="Trigger Name",
        )

    def test_trigger_definition_create(self):
        """Test trigger definition create."""
        self.assertEqual(
            self.trigger_definition.type, TriggerDefinitionTypeChoices.NAMED_EVENT
        )
        self.assertEqual(self.trigger_definition.name, "Trigger Name")

    def test_trigger_definition_update(self):
        """Test trigger definition update."""
        self.trigger_definition.name = "Updated Trigger Name"
        self.trigger_definition.save()
        self.assertEqual(self.trigger_definition.name, "Updated Trigger Name")

    def test_trigger_definition_delete(self):
        """Test trigger definition delete."""
        self.trigger_definition.delete()
        self.assertFalse(TriggerDefinition.objects.exists())
