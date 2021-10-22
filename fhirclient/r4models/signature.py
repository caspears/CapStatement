#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Signature) on 2018-12-20.
#  2018, SMART Health IT.


from . import element

class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..
    
    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    
    resource_type = "Signature"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.data = None
        
        """ The actual signature content (XML DigSig. JWS, picture, etc.).
        Type `str`. """
        
        self._data = None
        
        """ extension for fhir primitive  data"""
        
        self.onBehalfOf = None
        
        """ The party represented.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sigFormat = None
        
        """ The technical format of the signature.
        Type `str`. """
        
        self._sigFormat = None
        
        """ extension for fhir primitive  sigFormat"""
        
        self.targetFormat = None
        
        """ The technical format of the signed resources.
        Type `str`. """
        
        self._targetFormat = None
        
        """ extension for fhir primitive  targetFormat"""
        
        self.type = None
        
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.when = None
        
        """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.who = None
        
        """ Who signed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Signature, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("_data", "_data",fhirprimitive.FHIRPrimitive, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("sigFormat", "sigFormat", str, False, None, False),
            ("_sigFormat", "_sigFormat",fhirprimitive.FHIRPrimitive, False, None, False),
            ("targetFormat", "targetFormat", str, False, None, False),
            ("_targetFormat", "_targetFormat",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", coding.Coding, True, None, True),
            ("when", "when", fhirdate.FHIRDate, False, None, True),
            ("who", "who", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import fhirprimitive

