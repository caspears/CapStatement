#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    
    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    
    resource_type = "Immunization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doseQuantity = None
        
        """ Amount of vaccine administered.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.education = None
        
        """ Educational material presented to patient.
        List of `ImmunizationEducation` items (represented as `dict` in JSON). """
        
        self.encounter = None
        
        """ Encounter immunization was part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.expirationDate = None
        
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fundingSource = None
        
        """ Funding source for the vaccine.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.isSubpotent = None
        
        """ Dose potency.
        Type `bool`. """
        
        self._isSubpotent = None
        
        """ extension for fhir primitive  isSubpotent"""
        
        self.location = None
        
        """ Where immunization occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        
        """ Vaccine lot number.
        Type `str`. """
        
        self._lotNumber = None
        
        """ extension for fhir primitive  lotNumber"""
        
        self.manufacturer = None
        
        """ Vaccine manufacturer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note = None
        
        """ Additional immunization notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        
        """ Vaccine administration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrenceString = None
        
        """ Vaccine administration date.
        Type `str`. """
        
        self._occurrenceString = None
        
        """ extension for fhir primitive  occurrenceString"""
        
        self.patient = None
        
        """ Who was immunized.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        
        """ Who performed event.
        List of `ImmunizationPerformer` items (represented as `dict` in JSON). """
        
        self.primarySource = None
        
        """ Indicates context the data was recorded in.
        Type `bool`. """
        
        self._primarySource = None
        
        """ extension for fhir primitive  primarySource"""
        
        self.programEligibility = None
        
        """ Patient eligibility for a vaccination program.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.protocolApplied = None
        
        """ Protocol followed by the provider.
        List of `ImmunizationProtocolApplied` items (represented as `dict` in JSON). """
        
        self.reaction = None
        
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why immunization occurred.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recorded = None
        
        """ When the immunization was first captured in the subject's record.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reportOrigin = None
        
        """ Indicates the source of a secondarily reported record.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route = None
        
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ completed | entered-in-error | not-done.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.statusReason = None
        
        """ Reason not done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subpotentReason = None
        
        """ Reason for being subpotent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Immunization, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("fundingSource", "fundingSource", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("_isSubpotent", "_isSubpotent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("_lotNumber", "_lotNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", True),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", True),
            ("_occurrenceString", "_occurrenceString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("_primarySource", "_primarySource",fhirprimitive.FHIRPrimitive, False, None, False),
            ("programEligibility", "programEligibility", codeableconcept.CodeableConcept, True, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, False),
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subpotentReason", "subpotentReason", codeableconcept.CodeableConcept, True, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationEducation(backboneelement.BackboneElement):
    """ Educational material presented to patient.
    
    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    
    resource_type = "ImmunizationEducation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentType = None
        
        """ Educational material document identifier.
        Type `str`. """
        
        self._documentType = None
        
        """ extension for fhir primitive  documentType"""
        
        self.presentationDate = None
        
        """ Educational material presentation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publicationDate = None
        
        """ Educational material publication date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reference = None
        
        """ Educational material reference pointer.
        Type `str`. """
        
        self._reference = None
        
        """ extension for fhir primitive  reference"""
        
        super(ImmunizationEducation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", str, False, None, False),
            ("_documentType", "_documentType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("presentationDate", "presentationDate", fhirdate.FHIRDate, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("_reference", "_reference",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ImmunizationPerformer(backboneelement.BackboneElement):
    """ Who performed event.
    
    Indicates who performed the immunization event.
    """
    
    resource_type = "ImmunizationPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        
        """ Individual or organization who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function = None
        
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationPerformer, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ Protocol followed by the provider.
    
    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    
    resource_type = "ImmunizationProtocolApplied"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.doseNumberPositiveInt = None
        
        """ Dose number within series.
        Type `int`. """
        
        self._doseNumberPositiveInt = None
        
        """ extension for fhir primitive  doseNumberPositiveInt"""
        
        self.doseNumberString = None
        
        """ Dose number within series.
        Type `str`. """
        
        self._doseNumberString = None
        
        """ extension for fhir primitive  doseNumberString"""
        
        self.series = None
        
        """ Name of vaccine series.
        Type `str`. """
        
        self._series = None
        
        """ extension for fhir primitive  series"""
        
        self.seriesDosesPositiveInt = None
        
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self._seriesDosesPositiveInt = None
        
        """ extension for fhir primitive  seriesDosesPositiveInt"""
        
        self.seriesDosesString = None
        
        """ Recommended number of doses for immunity.
        Type `str`. """
        
        self._seriesDosesString = None
        
        """ extension for fhir primitive  seriesDosesString"""
        
        self.targetDisease = None
        
        """ Vaccine preventatable disease being targetted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationProtocolApplied, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", True),
            ("_doseNumberPositiveInt", "_doseNumberPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", True),
            ("_doseNumberString", "_doseNumberString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("series", "series", str, False, None, False),
            ("_series", "_series",fhirprimitive.FHIRPrimitive, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("_seriesDosesPositiveInt", "_seriesDosesPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("_seriesDosesString", "_seriesDosesString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.
    
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    
    resource_type = "ImmunizationReaction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        
        """ When reaction started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        
        """ Additional information on reaction.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reported = None
        
        """ Indicates self-reported reaction.
        Type `bool`. """
        
        self._reported = None
        
        """ extension for fhir primitive  reported"""
        
        super(ImmunizationReaction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
            ("_reported", "_reported",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import fhirprimitive

