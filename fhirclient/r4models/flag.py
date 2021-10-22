#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Flag) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Flag(domainresource.DomainResource):
    """ Key information to flag to healthcare providers.
    
    Prospective warnings of potential issues when providing care to the
    patient.
    """
    
    resource_type = "Flag"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        
        """ Flag creator.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Clinical, administrative, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Coded or textual message to display to user.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        
        """ Alert relevant during encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.period = None
        
        """ Time period when flag is active.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | inactive | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ Who/What is flag about?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Flag, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive

