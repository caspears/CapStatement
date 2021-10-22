#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    
    resource_type = "AppointmentResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        
        """ Person, Location, HealthcareService, or Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.appointment = None
        
        """ Appointment this response relates to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.comment = None
        
        """ Additional comments.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.end = None
        
        """ Time from appointment, or requested new end time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.participantStatus = None
        
        """ accepted | declined | tentative | in-process | completed | needs-
        action | entered-in-error.
        Type `str`. """
        
        self._participantStatus = None
        
        """ extension for fhir primitive  participantStatus"""
        
        self.participantType = None
        
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.start = None
        
        """ Time from appointment, or requested new start time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(AppointmentResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("participantStatus", "participantStatus", str, False, None, True),
            ("_participantStatus", "_participantStatus",fhirprimitive.FHIRPrimitive, False, None, False),
            ("participantType", "participantType", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import fhirprimitive

