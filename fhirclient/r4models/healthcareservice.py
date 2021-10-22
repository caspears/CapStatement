#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    
    resource_type = "HealthcareService"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        
        """ Whether this HealthcareService record is in active use.
        Type `bool`. """
        
        self._active = None
        
        """ extension for fhir primitive  active"""
        
        self.appointmentRequired = None
        
        """ If an appointment is required for access to this service.
        Type `bool`. """
        
        self._appointmentRequired = None
        
        """ extension for fhir primitive  appointmentRequired"""
        
        self.availabilityExceptions = None
        
        """ Description of availability exceptions.
        Type `str`. """
        
        self._availabilityExceptions = None
        
        """ extension for fhir primitive  availabilityExceptions"""
        
        self.availableTime = None
        
        """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Broad category of service being performed or delivered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        
        """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.comment = None
        
        """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.communication = None
        
        """ The language that this service is offered in.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.coverageArea = None
        
        """ Location(s) service is intended for/available to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.eligibility = None
        
        """ Specific eligibility requirements required to use the service.
        List of `HealthcareServiceEligibility` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        
        """ Technical endpoints providing access to electronic services
        operated for the healthcare service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.extraDetails = None
        
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
        
        self._extraDetails = None
        
        """ extension for fhir primitive  extraDetails"""
        
        self.identifier = None
        
        """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        
        """ Location(s) where service may be provided.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Description of service as presented to a consumer while searching.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.notAvailable = None
        
        """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        
        self.photo = None
        
        """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.program = None
        
        """ Programs that this service is applicable to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.providedBy = None
        
        """ Organization that provides this service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referralMethod = None
        
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceProvisionCode = None
        
        """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        
        """ Specialties handled by the HealthcareService.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        
        """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of service that may be delivered or performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active",fhirprimitive.FHIRPrimitive, False, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("_appointmentRequired", "_appointmentRequired",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("_availabilityExceptions", "_availabilityExceptions",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("_extraDetails", "_extraDetails",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("program", "program", codeableconcept.CodeableConcept, True, None, False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times that the Service Site is available.
    """
    
    resource_type = "HealthcareServiceAvailableTime"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        
        """ Always available? e.g. 24 hour service.
        Type `bool`. """
        
        self._allDay = None
        
        """ extension for fhir primitive  allDay"""
        
        self.availableEndTime = None
        
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.availableStartTime = None
        
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None
        
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        self._daysOfWeek = None
        
        """ extension for fhir primitive  daysOfWeek"""
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("_allDay", "_allDay",fhirprimitive.FHIRPrimitive, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("_daysOfWeek", "_daysOfWeek",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ Specific eligibility requirements required to use the service.
    
    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    
    resource_type = "HealthcareServiceEligibility"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Coded value for the eligibility.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment = None
        
        """ Describes the eligibility conditions for the service.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        super(HealthcareServiceEligibility, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    
    resource_type = "HealthcareServiceNotAvailable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Reason presented to the user explaining why time not available.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.during = None
        
        """ Service not available from this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("during", "during", period.Period, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive

