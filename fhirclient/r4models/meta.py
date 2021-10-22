#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Meta) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Meta(element.Element):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    
    resource_type = "Meta"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.lastUpdated = None
        
        """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.profile = None
        
        """ Profiles this resource claims to conform to.
        List of `str` items. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        self.security = None
        
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.source = None
        
        """ Identifies where the resource comes from.
        Type `str`. """
        
        self._source = None
        
        """ extension for fhir primitive  source"""
        
        self.tag = None
        
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.versionId = None
        
        """ Version specific identifier.
        Type `str`. """
        
        self._versionId = None
        
        """ extension for fhir primitive  versionId"""
        
        super(Meta, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("_profile", "_profile",fhirprimitive.FHIRPrimitive, False, None, False),
            ("security", "security", coding.Coding, True, None, False),
            ("source", "source", str, False, None, False),
            ("_source", "_source",fhirprimitive.FHIRPrimitive, False, None, False),
            ("tag", "tag", coding.Coding, True, None, False),
            ("versionId", "versionId", str, False, None, False),
            ("_versionId", "_versionId",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirprimitive

