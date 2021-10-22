#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Coding) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """
    
    resource_type = "Coding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Symbol in syntax defined by the system.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.display = None
        
        """ Representation defined by the system.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.system = None
        
        """ Identity of the terminology system.
        Type `str`. """
        
        self._system = None
        
        """ extension for fhir primitive  system"""
        
        self.userSelected = None
        
        """ If this coding was chosen directly by the user.
        Type `bool`. """
        
        self._userSelected = None
        
        """ extension for fhir primitive  userSelected"""
        
        self.version = None
        
        """ Version of the system - if relevant.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(Coding, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system",fhirprimitive.FHIRPrimitive, False, None, False),
            ("userSelected", "userSelected", bool, False, None, False),
            ("_userSelected", "_userSelected",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirprimitive

