#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/MoneyQuantity) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Quantity(element.Element):
    """ A measured or measurable amount.
    
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    
    resource_type = "Quantity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Coded form of the unit.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.comparator = None
        
        """ < | <= | >= | > - how to understand the value.
        Type `str`. """
        
        self._comparator = None
        
        """ extension for fhir primitive  comparator"""
        
        self.system = None
        
        """ System that defines coded unit form.
        Type `str`. """
        
        self._system = None
        
        """ extension for fhir primitive  system"""
        
        self.unit = None
        
        """ Unit representation.
        Type `str`. """
        
        self._unit = None
        
        """ extension for fhir primitive  unit"""
        
        self.value = None
        
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(Quantity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("comparator", "comparator", str, False, None, False),
            ("_comparator", "_comparator",fhirprimitive.FHIRPrimitive, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system",fhirprimitive.FHIRPrimitive, False, None, False),
            ("unit", "unit", str, False, None, False),
            ("_unit", "_unit",fhirprimitive.FHIRPrimitive, False, None, False),
            ("value", "value", float, False, None, False),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirprimitive

