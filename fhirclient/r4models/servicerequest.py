#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ServiceRequest) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.
    
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    
    resource_type = "ServiceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asNeededBoolean = None
        
        """ Preconditions for service.
        Type `bool`. """
        
        self._asNeededBoolean = None
        
        """ extension for fhir primitive  asNeededBoolean"""
        
        self.asNeededCodeableConcept = None
        
        """ Preconditions for service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        
        """ Date request signed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        
        """ Location on Body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Classification of service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        
        """ What is being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doNotPerform = None
        
        """ True if service/procedure should not be performed.
        Type `bool`. """
        
        self._doNotPerform = None
        
        """ extension for fhir primitive  doNotPerform"""
        
        self.encounter = None
        
        """ Encounter in which the request was created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Identifiers assigned to this order.
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
        
        """ proposal | plan | order +.
        Type `str`. """
        
        self._intent = None
        
        """ extension for fhir primitive  intent"""
        
        self.locationCode = None
        
        """ Requested location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.locationReference = None
        
        """ Requested location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        
        """ When service should occur.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        
        """ When service should occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        
        """ When service should occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.orderDetail = None
        
        """ Additional order information.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patientInstruction = None
        
        """ Patient or consumer-oriented instructions.
        Type `str`. """
        
        self._patientInstruction = None
        
        """ extension for fhir primitive  patientInstruction"""
        
        self.performer = None
        
        """ Requested performer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performerType = None
        
        """ Performer role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        self.quantityQuantity = None
        
        """ Service amount.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantityRange = None
        
        """ Service amount.
        Type `Range` (represented as `dict` in JSON). """
        
        self.quantityRatio = None
        
        """ Service amount.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        
        """ Explanation/Justification for procedure or service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Explanation/Justification for service or service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        
        """ Who/what is requesting service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requisition = None
        
        """ Composite Request ID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.specimen = None
        
        """ Procedure Samples.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | suspended | completed | entered-in-error |
        cancelled.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ Individual or Entity the service is ordered for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ServiceRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("_asNeededBoolean", "_asNeededBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("_doNotPerform", "_doNotPerform",fhirprimitive.FHIRPrimitive, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("locationCode", "locationCode", codeableconcept.CodeableConcept, True, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("orderDetail", "orderDetail", codeableconcept.CodeableConcept, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("_patientInstruction", "_patientInstruction",fhirprimitive.FHIRPrimitive, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, False, "quantity", False),
            ("quantityRange", "quantityRange", range.Range, False, "quantity", False),
            ("quantityRatio", "quantityRatio", ratio.Ratio, False, "quantity", False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
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
from . import ratio
from . import timing
from . import fhirprimitive

