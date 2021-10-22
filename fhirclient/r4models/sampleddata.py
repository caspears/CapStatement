#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/SampledData) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class SampledData(element.Element):
    """ A series of measurements taken by a device.
    
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    
    resource_type = "SampledData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.data = None
        
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """
        
        self._data = None
        
        """ extension for fhir primitive  data"""
        
        self.dimensions = None
        
        """ Number of sample points at each time point.
        Type `int`. """
        
        self._dimensions = None
        
        """ extension for fhir primitive  dimensions"""
        
        self.factor = None
        
        """ Multiply data by this before adding to origin.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.lowerLimit = None
        
        """ Lower limit of detection.
        Type `float`. """
        
        self._lowerLimit = None
        
        """ extension for fhir primitive  lowerLimit"""
        
        self.origin = None
        
        """ Zero value and units.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.period = None
        
        """ Number of milliseconds between samples.
        Type `float`. """
        
        self._period = None
        
        """ extension for fhir primitive  period"""
        
        self.upperLimit = None
        
        """ Upper limit of detection.
        Type `float`. """
        
        self._upperLimit = None
        
        """ extension for fhir primitive  upperLimit"""
        
        super(SampledData, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("_data", "_data",fhirprimitive.FHIRPrimitive, False, None, False),
            ("dimensions", "dimensions", int, False, None, True),
            ("_dimensions", "_dimensions",fhirprimitive.FHIRPrimitive, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("lowerLimit", "lowerLimit", float, False, None, False),
            ("_lowerLimit", "_lowerLimit",fhirprimitive.FHIRPrimitive, False, None, False),
            ("origin", "origin", quantity.Quantity, False, None, True),
            ("period", "period", float, False, None, True),
            ("_period", "_period",fhirprimitive.FHIRPrimitive, False, None, False),
            ("upperLimit", "upperLimit", float, False, None, False),
            ("_upperLimit", "_upperLimit",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import quantity
from . import fhirprimitive

