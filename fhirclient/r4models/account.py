#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Account) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Account(domainresource.DomainResource):
    """ Tracks balance, charges, for patient or cost center.
    
    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """
    
    resource_type = "Account"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        
        """ The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.
        List of `AccountCoverage` items (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Explanation of purpose/use.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.guarantor = None
        
        """ Responsible for the account.
        List of `AccountGuarantor` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Account number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Human-readable label.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.owner = None
        
        """ Who is responsible?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partOf = None
        
        """ Reference to a parent Account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.servicePeriod = None
        
        """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | inactive | entered-in-error | on-hold | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ What is account tied to?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Account, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("coverage", "coverage", AccountCoverage, True, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("guarantor", "guarantor", AccountGuarantor, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("servicePeriod", "servicePeriod", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class AccountCoverage(backboneelement.BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """
    
    resource_type = "AccountCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        
        """ The party(s), such as insurances, that may contribute to the
        payment of this account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ The priority of the coverage in the context of this account.
        Type `int`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("priority", "priority", int, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class AccountGuarantor(backboneelement.BackboneElement):
    """ Responsible for the account.
    
    Parties financially responsible for the account.
    """
    
    resource_type = "AccountGuarantor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.onHold = None
        
        """ Credit or other hold applied.
        Type `bool`. """
        
        self._onHold = None
        
        """ extension for fhir primitive  onHold"""
        
        self.party = None
        
        """ Responsible entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        
        """ Guarantee account during.
        Type `Period` (represented as `dict` in JSON). """
        
        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("onHold", "onHold", bool, False, None, False),
            ("_onHold", "_onHold",fhirprimitive.FHIRPrimitive, False, None, False),
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive

