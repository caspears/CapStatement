#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.
    
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    
    resource_type = "ObservationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abnormalCodedValueSet = None
        
        """ Value set of abnormal coded values for the observations conforming
        to this ObservationDefinition.
        Type `str`. """
        
        self._abnormalCodedValueSet = None
        
        """ extension for fhir primitive  abnormalCodedValueSet"""
        
        self.category = None
        
        """ Category of observation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criticalCodedValueSet = None
        
        """ Value set of critical coded values for the observations conforming
        to this ObservationDefinition.
        Type `str`. """
        
        self._criticalCodedValueSet = None
        
        """ extension for fhir primitive  criticalCodedValueSet"""
        
        self.identifier = None
        
        """ Business identifier for this ObservationDefinition instance.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.method = None
        
        """ Method used to produce the observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleResultsAllowed = None
        
        """ Multiple results allowed.
        Type `bool`. """
        
        self._multipleResultsAllowed = None
        
        """ extension for fhir primitive  multipleResultsAllowed"""
        
        self.normalCodedValueSet = None
        
        """ Value set of normal coded values for the observations conforming to
        this ObservationDefinition.
        Type `str`. """
        
        self._normalCodedValueSet = None
        
        """ extension for fhir primitive  normalCodedValueSet"""
        
        self.permittedDataType = None
        
        """ Quantity | CodeableConcept | string | boolean | integer | Range |
        Ratio | SampledData | time | dateTime | Period.
        List of `str` items. """
        
        self._permittedDataType = None
        
        """ extension for fhir primitive  permittedDataType"""
        
        self.preferredReportName = None
        
        """ Preferred report name.
        Type `str`. """
        
        self._preferredReportName = None
        
        """ extension for fhir primitive  preferredReportName"""
        
        self.qualifiedInterval = None
        
        """ Qualified range for continuous and ordinal observation results.
        List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON). """
        
        self.quantitativeDetails = None
        
        """ Characteristics of quantitative results.
        Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON). """
        
        self.validCodedValueSet = None
        
        """ Value set of valid coded values for the observations conforming to
        this ObservationDefinition.
        Type `str`. """
        
        self._validCodedValueSet = None
        
        """ extension for fhir primitive  validCodedValueSet"""
        
        super(ObservationDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("abnormalCodedValueSet", "abnormalCodedValueSet", str, False, None, False),
            ("_abnormalCodedValueSet", "_abnormalCodedValueSet",fhirprimitive.FHIRPrimitive, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("criticalCodedValueSet", "criticalCodedValueSet", str, False, None, False),
            ("_criticalCodedValueSet", "_criticalCodedValueSet",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("_multipleResultsAllowed", "_multipleResultsAllowed",fhirprimitive.FHIRPrimitive, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", str, False, None, False),
            ("_normalCodedValueSet", "_normalCodedValueSet",fhirprimitive.FHIRPrimitive, False, None, False),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("_permittedDataType", "_permittedDataType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("_preferredReportName", "_preferredReportName",fhirprimitive.FHIRPrimitive, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("validCodedValueSet", "validCodedValueSet", str, False, None, False),
            ("_validCodedValueSet", "_validCodedValueSet",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Qualified range for continuous and ordinal observation results.
    
    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    
    resource_type = "ObservationDefinitionQualifiedInterval"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.age = None
        
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.appliesTo = None
        
        """ Targetted population of the range.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        
        """ reference | critical | absolute.
        Type `str`. """
        
        self._category = None
        
        """ extension for fhir primitive  category"""
        
        self.condition = None
        
        """ Condition associated with the reference range.
        Type `str`. """
        
        self._condition = None
        
        """ extension for fhir primitive  condition"""
        
        self.context = None
        
        """ Range context qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.gender = None
        
        """ male | female | other | unknown.
        Type `str`. """
        
        self._gender = None
        
        """ extension for fhir primitive  gender"""
        
        self.gestationalAge = None
        
        """ Applicable gestational age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.range = None
        
        """ The interval itself, for continuous or ordinal observations.
        Type `Range` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQualifiedInterval, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", str, False, None, False),
            ("_category", "_category",fhirprimitive.FHIRPrimitive, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("_condition", "_condition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("context", "context", codeableconcept.CodeableConcept, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender",fhirprimitive.FHIRPrimitive, False, None, False),
            ("gestationalAge", "gestationalAge", range.Range, False, None, False),
            ("range", "range", range.Range, False, None, False),
        ])
        return js


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.
    
    Characteristics for quantitative results of this observation.
    """
    
    resource_type = "ObservationDefinitionQuantitativeDetails"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conversionFactor = None
        
        """ SI to Customary unit conversion factor.
        Type `float`. """
        
        self._conversionFactor = None
        
        """ extension for fhir primitive  conversionFactor"""
        
        self.customaryUnit = None
        
        """ Customary unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decimalPrecision = None
        
        """ Decimal precision of observation quantitative results.
        Type `int`. """
        
        self._decimalPrecision = None
        
        """ extension for fhir primitive  decimalPrecision"""
        
        self.unit = None
        
        """ SI unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQuantitativeDetails, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("_conversionFactor", "_conversionFactor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("customaryUnit", "customaryUnit", codeableconcept.CodeableConcept, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
            ("_decimalPrecision", "_decimalPrecision",fhirprimitive.FHIRPrimitive, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import identifier
from . import range
from . import fhirprimitive

