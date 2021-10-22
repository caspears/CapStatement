#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.
    
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    
    resource_type = "DeviceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.codeCodeableConcept = None
        
        """ Device requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.codeReference = None
        
        """ Device requested.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        
        """ Encounter motivating request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        
        """ Identifier of composite request.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ External Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self._instantiatesCanonical = None
        
        """ extension for fhir primitive  instantiatesCanonical"""
        
        self.instantiatesUri = None
        
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self._instantiatesUri = None
        
        """ extension for fhir primitive  instantiatesUri"""
        
        self.insurance = None
        
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent = None
        
        """ proposal | plan | original-order | encoded | reflex-order.
        Type `str`. """
        
        self._intent = None
        
        """ extension for fhir primitive  intent"""
        
        self.note = None
        
        """ Notes or comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        
        """ Desired time or schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        
        """ Desired time or schedule for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        
        """ Desired time or schedule for use.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.parameter = None
        
        """ Device details.
        List of `DeviceRequestParameter` items (represented as `dict` in JSON). """
        
        self.performer = None
        
        """ Requested Filler.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType = None
        
        """ Filler role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priorRequest = None
        
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ Indicates how quickly the {{title}} should be addressed with
        respect to other requests.
        Type `str`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        self.reasonCode = None
        
        """ Coded Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Linked Reason for request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        
        """ Who/what is requesting diagnostics.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | suspended | completed | entered-in-error |
        cancelled.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ Focus of request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("codeCodeableConcept", "codeCodeableConcept", codeableconcept.CodeableConcept, False, "code", True),
            ("codeReference", "codeReference", fhirreference.FHIRReference, False, "code", True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("parameter", "parameter", DeviceRequestParameter, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priorRequest", "priorRequest", fhirreference.FHIRReference, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceRequestParameter(backboneelement.BackboneElement):
    """ Device details.
    
    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    
    resource_type = "DeviceRequestParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Device detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        
        """ Value of detail.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCodeableConcept = None
        
        """ Value of detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        
        """ Value of detail.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        
        """ Value of detail.
        Type `Range` (represented as `dict` in JSON). """
        
        super(DeviceRequestParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import timing
from . import fhirprimitive

