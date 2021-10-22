#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Contributor) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Contributor(element.Element):
    """ Contributor information.
    
    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """
    
    resource_type = "Contributor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        
        """ Contact details of the contributor.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Who contributed the content.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.type = None
        
        """ author | editor | reviewer | endorser.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(Contributor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Contributor, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import contactdetail
from . import fhirprimitive

