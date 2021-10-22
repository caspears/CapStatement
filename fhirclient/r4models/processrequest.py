#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ProcessRequest) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ProcessRequest(domainresource.DomainResource):
    """ Request to perform some action on or in regard to an existing resource.
    
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """
    
    resource_type = "ProcessRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        
        """ cancel | poll | reprocess | status.
        Type `str`. """
        
        self._action = None
        
        """ extension for fhir primitive  action"""
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exclude = None
        
        """ Resource type(s) to exclude.
        List of `str` items. """
        
        self._exclude = None
        
        """ extension for fhir primitive  exclude"""
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.include = None
        
        """ Resource type(s) to include.
        List of `str` items. """
        
        self._include = None
        
        """ extension for fhir primitive  include"""
        
        self.item = None
        
        """ Items to re-adjudicate.
        List of `ProcessRequestItem` items (represented as `dict` in JSON). """
        
        self.nullify = None
        
        """ Remove history.
        Type `bool`. """
        
        self._nullify = None
        
        """ extension for fhir primitive  nullify"""
        
        self.period = None
        
        """ Selection period.
        Type `Period` (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reference = None
        
        """ Reference number/string.
        Type `str`. """
        
        self._reference = None
        
        """ extension for fhir primitive  reference"""
        
        self.request = None
        
        """ Reference to the Request resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        
        """ Reference to the Response resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.target = None
        
        """ Party which is the target of the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcessRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcessRequest, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, False),
            ("_action", "_action",fhirprimitive.FHIRPrimitive, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("exclude", "exclude", str, True, None, False),
            ("_exclude", "_exclude",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("include", "include", str, True, None, False),
            ("_include", "_include",fhirprimitive.FHIRPrimitive, False, None, False),
            ("item", "item", ProcessRequestItem, True, None, False),
            ("nullify", "nullify", bool, False, None, False),
            ("_nullify", "_nullify",fhirprimitive.FHIRPrimitive, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("_reference", "_reference",fhirprimitive.FHIRPrimitive, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class ProcessRequestItem(backboneelement.BackboneElement):
    """ Items to re-adjudicate.
    
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """
    
    resource_type = "ProcessRequestItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequenceLinkId = None
        
        """ Service instance.
        Type `int`. """
        
        self._sequenceLinkId = None
        
        """ extension for fhir primitive  sequenceLinkId"""
        
        super(ProcessRequestItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcessRequestItem, self).elementProperties()
        js.extend([
            ("sequenceLinkId", "sequenceLinkId", int, False, None, True),
            ("_sequenceLinkId", "_sequenceLinkId",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive

