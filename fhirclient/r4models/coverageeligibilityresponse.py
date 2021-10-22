#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class CoverageEligibilityResponse(domainresource.DomainResource):
    """ CoverageEligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """
    
    resource_type = "CoverageEligibilityResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        
        """ Disposition Message.
        Type `str`. """
        
        self._disposition = None
        
        """ extension for fhir primitive  disposition"""
        
        self.error = None
        
        """ Processing errors.
        List of `CoverageEligibilityResponseError` items (represented as `dict` in JSON). """
        
        self.form = None
        
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance = None
        
        """ Details by insurance coverage.
        List of `CoverageEligibilityResponseInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        
        """ Insurer issuing the coverage.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        
        """ queued | complete | error | partial.
        Type `str`. """
        
        self._outcome = None
        
        """ extension for fhir primitive  outcome"""
        
        self.patient = None
        
        """ The subject of the Products and Services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        
        """ Pre-Authorization/Determination Reference.
        Type `str`. """
        
        self._preAuthRef = None
        
        """ extension for fhir primitive  preAuthRef"""
        
        self.purpose = None
        
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.request = None
        
        """ Eligibility reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        
        """ Responsible provider.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        
        """ Estimated date or dates for inquiry.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        
        """ Estimated date or dates for inquiry.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(CoverageEligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("error", "error", CoverageEligibilityResponseError, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("_preAuthRef", "_preAuthRef",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    resource_type = "CoverageEligibilityResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Details by insurance coverage.
    
    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """
    
    resource_type = "CoverageEligibilityResponseInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contract = None
        
        """ Contract details.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage = None
        
        """ Updated Coverage details.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.inforce = None
        
        """ Coverage inforce indicator.
        Type `bool`. """
        
        self._inforce = None
        
        """ extension for fhir primitive  inforce"""
        
        self.item = None
        
        """ Benefits and Authorization requirements by Category or Service.
        List of `CoverageEligibilityResponseInsuranceItem` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("contract", "contract", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("inforce", "inforce", bool, False, None, False),
            ("_inforce", "_inforce",fhirprimitive.FHIRPrimitive, False, None, False),
            ("item", "item", CoverageEligibilityResponseInsuranceItem, True, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """ Benefits and Authorization requirements by Category or Service.
    
    Benefits and optionally current balances by Category or Service.
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorizationRequired = None
        
        """ Authorization required flag.
        Type `bool`. """
        
        self._authorizationRequired = None
        
        """ extension for fhir primitive  authorizationRequired"""
        
        self.authorizationSupporting = None
        
        """ Codes or text of materials to be submitted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.authorizationUrl = None
        
        """ Pre-authorization requirements.
        Type `str`. """
        
        self._authorizationUrl = None
        
        """ extension for fhir primitive  authorizationUrl"""
        
        self.benefit = None
        
        """ Benefit Summary.
        List of `CoverageEligibilityResponseInsuranceItemBenefit` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Type of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Description of the benefit or services covered.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.excluded = None
        
        """ Excluded from the plan.
        Type `bool`. """
        
        self._excluded = None
        
        """ extension for fhir primitive  excluded"""
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Short name for the benefit.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.network = None
        
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Performing practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.term = None
        
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsuranceItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend([
            ("authorizationRequired", "authorizationRequired", bool, False, None, False),
            ("_authorizationRequired", "_authorizationRequired",fhirprimitive.FHIRPrimitive, False, None, False),
            ("authorizationSupporting", "authorizationSupporting", codeableconcept.CodeableConcept, True, None, False),
            ("authorizationUrl", "authorizationUrl", str, False, None, False),
            ("_authorizationUrl", "_authorizationUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("benefit", "benefit", CoverageEligibilityResponseInsuranceItemBenefit, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("_excluded", "_excluded",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits used to date.
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItemBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedMoney = None
        
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        
        self.allowedString = None
        
        """ Benefits allowed.
        Type `str`. """
        
        self._allowedString = None
        
        """ extension for fhir primitive  allowedString"""
        
        self.allowedUnsignedInt = None
        
        """ Benefits allowed.
        Type `int`. """
        
        self._allowedUnsignedInt = None
        
        """ extension for fhir primitive  allowedUnsignedInt"""
        
        self.type = None
        
        """ Deductible, visits, benefit amount.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usedMoney = None
        
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        
        self.usedUnsignedInt = None
        
        """ Benefits used.
        Type `int`. """
        
        self._usedUnsignedInt = None
        
        """ extension for fhir primitive  usedUnsignedInt"""
        
        super(CoverageEligibilityResponseInsuranceItemBenefit, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItemBenefit, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("_allowedString", "_allowedString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("_allowedUnsignedInt", "_allowedUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
            ("_usedUnsignedInt", "_usedUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import fhirprimitive

