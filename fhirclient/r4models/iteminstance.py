#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ItemInstance) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ItemInstance(domainresource.DomainResource):
    """ A physical instance of an item.
    
    A physical, countable instance of an item, for example one box or one unit.
    """
    
    resource_type = "ItemInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.carrierAIDC = None
        
        """ The machine-readable AIDC string in base64 encoding.
        Type `str`. """
        
        self._carrierAIDC = None
        
        """ extension for fhir primitive  carrierAIDC"""
        
        self.carrierHRF = None
        
        """ The human-readable barcode string.
        Type `str`. """
        
        self._carrierHRF = None
        
        """ extension for fhir primitive  carrierHRF"""
        
        self.count = None
        
        """ The count of items.
        Type `int`. """
        
        self._count = None
        
        """ extension for fhir primitive  count"""
        
        self.currentSWVersion = None
        
        """ The Software version associated with the device.
        Type `str`. """
        
        self._currentSWVersion = None
        
        """ extension for fhir primitive  currentSWVersion"""
        
        self.expiryDate = None
        
        """ The expiry or preparation date and time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.location = None
        
        """ The physical location of the item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        
        """ The lot or batch number.
        Type `str`. """
        
        self._lotNumber = None
        
        """ extension for fhir primitive  lotNumber"""
        
        self.manufactureDate = None
        
        """ The manufacture or preparation date and time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.serialNumber = None
        
        """ The serial number if available.
        Type `str`. """
        
        self._serialNumber = None
        
        """ extension for fhir primitive  serialNumber"""
        
        self.subject = None
        
        """ The patient that the item is affixed to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ItemInstance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ItemInstance, self).elementProperties()
        js.extend([
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("_carrierAIDC", "_carrierAIDC",fhirprimitive.FHIRPrimitive, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("_carrierHRF", "_carrierHRF",fhirprimitive.FHIRPrimitive, False, None, False),
            ("count", "count", int, False, None, True),
            ("_count", "_count",fhirprimitive.FHIRPrimitive, False, None, False),
            ("currentSWVersion", "currentSWVersion", str, False, None, False),
            ("_currentSWVersion", "_currentSWVersion",fhirprimitive.FHIRPrimitive, False, None, False),
            ("expiryDate", "expiryDate", fhirdate.FHIRDate, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("_lotNumber", "_lotNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("_serialNumber", "_serialNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import fhirdate
from . import fhirreference
from . import fhirprimitive

