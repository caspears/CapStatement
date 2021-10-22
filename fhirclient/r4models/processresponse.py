#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ProcessResponse) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ProcessResponse(domainresource.DomainResource):
    """ ProcessResponse resource.
    
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """
    
    resource_type = "ProcessResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.communicationRequest = None
        
        """ Request for additional information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        
        """ Disposition Message.
        Type `str`. """
        
        self._disposition = None
        
        """ extension for fhir primitive  disposition"""
        
        self.error = None
        
        """ Error code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.form = None
        
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        
        """ Authoring Organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        
        """ Processing outcome.
        Type `str`. """
        
        self._outcome = None
        
        """ extension for fhir primitive  outcome"""
        
        self.processNote = None
        
        """ Processing comments or additional requirements.
        List of `ProcessResponseProcessNote` items (represented as `dict` in JSON). """
        
        self.request = None
        
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        
        """ Responsible Practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(ProcessResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcessResponse, self).elementProperties()
        js.extend([
            ("communicationRequest", "communicationRequest", fhirreference.FHIRReference, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("error", "error", codeableconcept.CodeableConcept, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome",fhirprimitive.FHIRPrimitive, False, None, False),
            ("processNote", "processNote", ProcessResponseProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ProcessResponseProcessNote(backboneelement.BackboneElement):
    """ Processing comments or additional requirements.
    
    Suite of processing notes or additional requirements if the processing has
    been held.
    """
    
    resource_type = "ProcessResponseProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        
        """ Comment on the processing.
        Type `str`. """
        
        self._text = None
        
        """ extension for fhir primitive  text"""
        
        self.type = None
        
        """ display | print | printoper.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(ProcessResponseProcessNote, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcessResponseProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("_text", "_text",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

