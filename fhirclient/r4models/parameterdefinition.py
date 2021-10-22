#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.
    
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    
    resource_type = "ParameterDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        
        """ A brief description of the parameter.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.max = None
        
        """ Maximum cardinality (a number of *).
        Type `str`. """
        
        self._max = None
        
        """ extension for fhir primitive  max"""
        
        self.min = None
        
        """ Minimum cardinality.
        Type `int`. """
        
        self._min = None
        
        """ extension for fhir primitive  min"""
        
        self.name = None
        
        """ Name used to access the parameter value.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.profile = None
        
        """ What profile the value is expected to be.
        Type `str`. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        self.type = None
        
        """ What type of value.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.use = None
        
        """ in | out.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        super(ParameterDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max",fhirprimitive.FHIRPrimitive, False, None, False),
            ("min", "min", int, False, None, False),
            ("_min", "_min",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirprimitive

