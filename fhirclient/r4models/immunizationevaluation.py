#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ImmunizationEvaluation(domainresource.DomainResource):
    """ Immunization evaluation information.
    
    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    
    resource_type = "ImmunizationEvaluation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date evaluation was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Evaluation notes.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
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
        
        self.doseStatus = None
        
        """ Status of the dose relative to published recommendations.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseStatusReason = None
        
        """ Reason for the dose status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.immunizationEvent = None
        
        """ Immunization being evaluated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        
        """ Who this evaluation is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.status = None
        
        """ completed | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.targetDisease = None
        
        """ Evaluation target disease.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationEvaluation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("_doseNumberPositiveInt", "_doseNumberPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("_doseNumberString", "_doseNumberString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False, None, True),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("immunizationEvent", "immunizationEvent", fhirreference.FHIRReference, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("series", "series", str, False, None, False),
            ("_series", "_series",fhirprimitive.FHIRPrimitive, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("_seriesDosesPositiveInt", "_seriesDosesPositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("_seriesDosesString", "_seriesDosesString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

