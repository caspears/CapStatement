#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Money) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Money(element.Element):
    """ An amount of economic utility in some recognized currency.
    """
    
    resource_type = "Money"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.currency = None
        
        """ ISO 4217 Currency Code.
        Type `str`. """
        
        self._currency = None
        
        """ extension for fhir primitive  currency"""
        
        self.value = None
        
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(Money, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend([
            ("currency", "currency", str, False, None, False),
            ("_currency", "_currency",fhirprimitive.FHIRPrimitive, False, None, False),
            ("value", "value", float, False, None, False),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirprimitive

