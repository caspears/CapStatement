#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/HumanName) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.
    
    A human's name with the ability to identify parts and usage.
    """
    
    resource_type = "HumanName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.family = None
        
        """ Family name (often called 'Surname').
        Type `str`. """
        
        self._family = None
        
        """ extension for fhir primitive  family"""
        
        self.given = None
        
        """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """
        
        self._given = None
        
        """ extension for fhir primitive  given"""
        
        self.period = None
        
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.prefix = None
        
        """ Parts that come before the name.
        List of `str` items. """
        
        self._prefix = None
        
        """ extension for fhir primitive  prefix"""
        
        self.suffix = None
        
        """ Parts that come after the name.
        List of `str` items. """
        
        self._suffix = None
        
        """ extension for fhir primitive  suffix"""
        
        self.text = None
        
        """ Text representation of the full name.
        Type `str`. """
        
        self._text = None
        
        """ extension for fhir primitive  text"""
        
        self.use = None
        
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        super(HumanName, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("family", "family", str, False, None, False),
            ("_family", "_family",fhirprimitive.FHIRPrimitive, False, None, False),
            ("given", "given", str, True, None, False),
            ("_given", "_given",fhirprimitive.FHIRPrimitive, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("_prefix", "_prefix",fhirprimitive.FHIRPrimitive, False, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("_suffix", "_suffix",fhirprimitive.FHIRPrimitive, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text",fhirprimitive.FHIRPrimitive, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import period
from . import fhirprimitive

