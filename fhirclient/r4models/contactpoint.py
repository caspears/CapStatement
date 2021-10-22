#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).
    
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    
    resource_type = "ContactPoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        
        """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.rank = None
        
        """ Specify preferred order of use (1 = highest).
        Type `int`. """
        
        self._rank = None
        
        """ extension for fhir primitive  rank"""
        
        self.system = None
        
        """ phone | fax | email | pager | url | sms | other.
        Type `str`. """
        
        self._system = None
        
        """ extension for fhir primitive  system"""
        
        self.use = None
        
        """ home | work | temp | old | mobile - purpose of this contact point.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        self.value = None
        
        """ The actual contact point details.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(ContactPoint, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ContactPoint, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("rank", "rank", int, False, None, False),
            ("_rank", "_rank",fhirprimitive.FHIRPrimitive, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system",fhirprimitive.FHIRPrimitive, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use",fhirprimitive.FHIRPrimitive, False, None, False),
            ("value", "value", str, False, None, False),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import period
from . import fhirprimitive

