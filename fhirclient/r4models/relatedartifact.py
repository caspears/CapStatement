#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.
    
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    
    resource_type = "RelatedArtifact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.citation = None
        
        """ Bibliographic citation for the artifact.
        Type `str`. """
        
        self._citation = None
        
        """ extension for fhir primitive  citation"""
        
        self.display = None
        
        """ Brief description of the related artifact.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.document = None
        
        """ What document is being referenced.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.label = None
        
        """ Short label.
        Type `str`. """
        
        self._label = None
        
        """ extension for fhir primitive  label"""
        
        self.resource = None
        
        """ What resource is being referenced.
        Type `str`. """
        
        self._resource = None
        
        """ extension for fhir primitive  resource"""
        
        self.type = None
        
        """ documentation | justification | citation | predecessor | successor
        | derived-from | depends-on | composed-of.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.url = None
        
        """ Where the artifact can be accessed.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        super(RelatedArtifact, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("citation", "citation", str, False, None, False),
            ("_citation", "_citation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("document", "document", attachment.Attachment, False, None, False),
            ("label", "label", str, False, None, False),
            ("_label", "_label",fhirprimitive.FHIRPrimitive, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("_resource", "_resource",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import attachment
from . import fhirprimitive

