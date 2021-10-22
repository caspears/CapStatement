#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Attachment) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Attachment(element.Element):
    """ Content in a format defined elsewhere.
    
    For referring to data content defined in other formats.
    """
    
    resource_type = "Attachment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        
        """ Mime type of the content, with charset etc..
        Type `str`. """
        
        self._contentType = None
        
        """ extension for fhir primitive  contentType"""
        
        self.creation = None
        
        """ Date attachment was first created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.data = None
        
        """ Data inline, base64ed.
        Type `str`. """
        
        self._data = None
        
        """ extension for fhir primitive  data"""
        
        self.hash = None
        
        """ Hash of the data (sha-1, base64ed).
        Type `str`. """
        
        self._hash = None
        
        """ extension for fhir primitive  hash"""
        
        self.language = None
        
        """ Human language of the content (BCP-47).
        Type `str`. """
        
        self._language = None
        
        """ extension for fhir primitive  language"""
        
        self.size = None
        
        """ Number of bytes of content (if url provided).
        Type `int`. """
        
        self._size = None
        
        """ extension for fhir primitive  size"""
        
        self.title = None
        
        """ Label to display in place of the data.
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Uri where the data can be found.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        super(Attachment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, False),
            ("_contentType", "_contentType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("creation", "creation", fhirdate.FHIRDate, False, None, False),
            ("data", "data", str, False, None, False),
            ("_data", "_data",fhirprimitive.FHIRPrimitive, False, None, False),
            ("hash", "hash", str, False, None, False),
            ("_hash", "_hash",fhirprimitive.FHIRPrimitive, False, None, False),
            ("language", "language", str, False, None, False),
            ("_language", "_language",fhirprimitive.FHIRPrimitive, False, None, False),
            ("size", "size", int, False, None, False),
            ("_size", "_size",fhirprimitive.FHIRPrimitive, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirdate
from . import fhirprimitive

