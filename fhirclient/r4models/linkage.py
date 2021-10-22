#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Linkage) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Linkage(domainresource.DomainResource):
    """ Links records for 'same' item.
    
    Identifies two or more records (resource instances) that are referring to
    the same real-world "occurrence".
    """
    
    resource_type = "Linkage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        
        """ Whether this linkage assertion is active or not.
        Type `bool`. """
        
        self._active = None
        
        """ extension for fhir primitive  active"""
        
        self.author = None
        
        """ Who is responsible for linkages.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Item to be linked.
        List of `LinkageItem` items (represented as `dict` in JSON). """
        
        super(Linkage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Linkage, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active",fhirprimitive.FHIRPrimitive, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("item", "item", LinkageItem, True, None, True),
        ])
        return js


from . import backboneelement

class LinkageItem(backboneelement.BackboneElement):
    """ Item to be linked.
    
    Identifies one of the records that is considered to refer to the same real-
    world occurrence as well as how the items should be evaluated within the
    collection of linked items.
    """
    
    resource_type = "LinkageItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resource = None
        
        """ Resource being linked.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ source | alternate | historical.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(LinkageItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LinkageItem, self).elementProperties()
        js.extend([
            ("resource", "resource", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirreference
from . import fhirprimitive

