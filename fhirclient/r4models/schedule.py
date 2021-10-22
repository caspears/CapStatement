#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Schedule) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Schedule(domainresource.DomainResource):
    """ A container for slots of time that may be available for booking
    appointments.
    """
    
    resource_type = "Schedule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        
        """ Whether this schedule is in active use.
        Type `bool`. """
        
        self._active = None
        
        """ extension for fhir primitive  active"""
        
        self.actor = None
        
        """ E.g. HealthCareService, Location, Practitioner, etc..
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.comment = None
        
        """ Comments on availability.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.identifier = None
        
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.planningHorizon = None
        
        """ Period of time covered by schedule.
        Type `Period` (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        
        """ High-level category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
        
        """ Specific service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        
        """ Type of specialty needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Schedule, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active",fhirprimitive.FHIRPrimitive, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, True, None, True),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("planningHorizon", "planningHorizon", period.Period, False, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
from . import fhirprimitive

