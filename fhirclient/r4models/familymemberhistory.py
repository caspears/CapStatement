#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.
    
    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """
    
    resource_type = "FamilyMemberHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageAge = None
        
        """ (approximate) age.
        Type `Age` (represented as `dict` in JSON). """
        
        self.ageRange = None
        
        """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """
        
        self.ageString = None
        
        """ (approximate) age.
        Type `str`. """
        
        self._ageString = None
        
        """ extension for fhir primitive  ageString"""
        
        self.bornDate = None
        
        """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.bornPeriod = None
        
        """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """
        
        self.bornString = None
        
        """ (approximate) date of birth.
        Type `str`. """
        
        self._bornString = None
        
        """ extension for fhir primitive  bornString"""
        
        self.condition = None
        
        """ Condition that the related person had.
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
        
        self.dataAbsentReason = None
        
        """ subject-unknown | withheld | unable-to-obtain | deferred.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        
        """ When history was recorded or last updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedAge = None
        
        """ Dead? How old/when?.
        Type `Age` (represented as `dict` in JSON). """
        
        self.deceasedBoolean = None
        
        """ Dead? How old/when?.
        Type `bool`. """
        
        self._deceasedBoolean = None
        
        """ extension for fhir primitive  deceasedBoolean"""
        
        self.deceasedDate = None
        
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedRange = None
        
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
        
        self.deceasedString = None
        
        """ Dead? How old/when?.
        Type `str`. """
        
        self._deceasedString = None
        
        """ extension for fhir primitive  deceasedString"""
        
        self.estimatedAge = None
        
        """ Age is estimated?.
        Type `bool`. """
        
        self._estimatedAge = None
        
        """ extension for fhir primitive  estimatedAge"""
        
        self.identifier = None
        
        """ External Id(s) for this record.
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
        
        self.name = None
        
        """ The family member described.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.note = None
        
        """ General note about related person.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patient = None
        
        """ Patient history is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        
        """ Why was family member history performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why was family member history performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relationship = None
        
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sex = None
        
        """ male | female | other | unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ partial | completed | entered-in-error | health-unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(FamilyMemberHistory, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageAge", "ageAge", age.Age, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("ageString", "ageString", str, False, "age", False),
            ("_ageString", "_ageString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("bornDate", "bornDate", fhirdate.FHIRDate, False, "born", False),
            ("bornPeriod", "bornPeriod", period.Period, False, "born", False),
            ("bornString", "bornString", str, False, "born", False),
            ("_bornString", "_bornString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deceasedAge", "deceasedAge", age.Age, False, "deceased", False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("_deceasedBoolean", "_deceasedBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("deceasedDate", "deceasedDate", fhirdate.FHIRDate, False, "deceased", False),
            ("deceasedRange", "deceasedRange", range.Range, False, "deceased", False),
            ("deceasedString", "deceasedString", str, False, "deceased", False),
            ("_deceasedString", "_deceasedString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("estimatedAge", "estimatedAge", bool, False, None, False),
            ("_estimatedAge", "_estimatedAge",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, True),
            ("sex", "sex", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    resource_type = "FamilyMemberHistoryCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contributedToDeath = None
        
        """ Whether the condition contributed to the cause of death.
        Type `bool`. """
        
        self._contributedToDeath = None
        
        """ extension for fhir primitive  contributedToDeath"""
        
        self.note = None
        
        """ Extra information about condition.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge = None
        
        """ When condition first manifested.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetPeriod = None
        
        """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        
        """ When condition first manifested.
        Type `str`. """
        
        self._onsetString = None
        
        """ extension for fhir primitive  onsetString"""
        
        self.outcome = None
        
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(FamilyMemberHistoryCondition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("contributedToDeath", "contributedToDeath", bool, False, None, False),
            ("_contributedToDeath", "_contributedToDeath",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("_onsetString", "_onsetString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import age
from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import fhirprimitive

