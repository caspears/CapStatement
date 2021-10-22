#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Narrative) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Narrative(element.Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).
    
    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """
    
    resource_type = "Narrative"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.div = None
        
        """ Limited xhtml content.
        Type `str`. """
        
        self._div = None
        
        """ extension for fhir primitive  div"""
        
        self.status = None
        
        """ generated | extensions | additional | empty.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(Narrative, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("div", "div", str, False, None, True),
            ("_div", "_div",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirprimitive

