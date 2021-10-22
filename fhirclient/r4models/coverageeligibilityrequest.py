#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class CoverageEligibilityRequest(domainresource.DomainResource):
    """ CoverageEligibilityRequest resource.
    
    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """
    
    resource_type = "CoverageEligibilityRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.enterer = None
        
        """ Author.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility = None
        
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance = None
        
        """ Patient's Insurance or medical plan(s).
        List of `CoverageEligibilityRequestInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Service types, codes and supporting information.
        List of `CoverageEligibilityRequestItem` items (represented as `dict` in JSON). """
        
        self.patient = None
        
        """ The subject of the Products and Services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Responsible provider.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.purpose = None
        
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.servicedDate = None
        
        """ Estimated date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        
        """ Estimated date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.supportingInfo = None
        
        """ Exceptions, special considerations, the condition, situation, prior
        or concurrent issues.
        List of `CoverageEligibilityRequestSupportingInfo` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityRequestInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", CoverageEligibilityRequestItem, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("supportingInfo", "supportingInfo", CoverageEligibilityRequestSupportingInfo, True, None, False),
        ])
        return js


from . import backboneelement

class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    """ Patient's Insurance or medical plan(s).
    
    Insurance policies which the patient has advised may be applicable for
    paying for health services.
    """
    
    resource_type = "CoverageEligibilityRequestInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
        
        """ Business agreement.
        Type `str`. """
        
        self._businessArrangement = None
        
        """ extension for fhir primitive  businessArrangement"""
        
        self.coverage = None
        
        """ Insurance or medical plan.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focal = None
        
        """ Is the focal Coverage.
        Type `bool`. """
        
        self._focal = None
        
        """ extension for fhir primitive  focal"""
        
        super(CoverageEligibilityRequestInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("_businessArrangement", "_businessArrangement",fhirprimitive.FHIRPrimitive, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, False),
            ("_focal", "_focal",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """ Service types, codes and supporting information.
    
    A list of service types or billable services for which bebefit details
    and/or an authorization prior to service delivery may be required by the
    payor.
    """
    
    resource_type = "CoverageEligibilityRequestItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Type of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        
        """ Product or service details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.diagnosis = None
        
        """ List of Diagnosis.
        List of `CoverageEligibilityRequestItemDiagnosis` items (represented as `dict` in JSON). """
        
        self.facility = None
        
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Perfoming practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.supportingInformationSequence = None
        
        """ Applicable exception and supporting information.
        List of `int` items. """
        
        self._supportingInformationSequence = None
        
        """ extension for fhir primitive  supportingInformationSequence"""
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequestItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
        js.extend([
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("diagnosis", "diagnosis", CoverageEligibilityRequestItemDiagnosis, True, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("supportingInformationSequence", "supportingInformationSequence", int, True, None, False),
            ("_supportingInformationSequence", "_supportingInformationSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """ List of Diagnosis.
    
    List of patient diagnosis for which care is sought.
    """
    
    resource_type = "CoverageEligibilityRequestItemDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        
        """ Patient's diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference = None
        
        """ Patient's diagnosis.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequestItemDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", False),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", False),
        ])
        return js


class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """
    
    resource_type = "CoverageEligibilityRequestSupportingInfo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appliesToAll = None
        
        """ Applies to all items.
        Type `bool`. """
        
        self._appliesToAll = None
        
        """ extension for fhir primitive  appliesToAll"""
        
        self.information = None
        
        """ Additional Data or supporting information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Information instance identifier.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        super(CoverageEligibilityRequestSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend([
            ("appliesToAll", "appliesToAll", bool, False, None, False),
            ("_appliesToAll", "_appliesToAll",fhirprimitive.FHIRPrimitive, False, None, False),
            ("information", "information", fhirreference.FHIRReference, False, None, True),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import fhirprimitive

