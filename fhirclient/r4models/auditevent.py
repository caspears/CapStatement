#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.
    
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    
    resource_type = "AuditEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        
        """ Type of action performed during the event.
        Type `str`. """
        
        self._action = None
        
        """ extension for fhir primitive  action"""
        
        self.agent = None
        
        """ Actor involved in the event.
        List of `AuditEventAgent` items (represented as `dict` in JSON). """
        
        self.entity = None
        
        """ Data or objects used.
        List of `AuditEventEntity` items (represented as `dict` in JSON). """
        
        self.outcome = None
        
        """ Whether the event succeeded or failed.
        Type `str`. """
        
        self._outcome = None
        
        """ extension for fhir primitive  outcome"""
        
        self.outcomeDesc = None
        
        """ Description of the event outcome.
        Type `str`. """
        
        self._outcomeDesc = None
        
        """ extension for fhir primitive  outcomeDesc"""
        
        self.period = None
        
        """ When the activity occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.purposeOfEvent = None
        
        """ The purposeOfUse of the event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recorded = None
        
        """ Time when the event was recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.source = None
        
        """ Audit Event Reporter.
        Type `AuditEventSource` (represented as `dict` in JSON). """
        
        self.subtype = None
        
        """ More specific type/id for the event.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type/identifier of event.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(AuditEvent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, False),
            ("_action", "_action",fhirprimitive.FHIRPrimitive, False, None, False),
            ("agent", "agent", AuditEventAgent, True, None, True),
            ("entity", "entity", AuditEventEntity, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome",fhirprimitive.FHIRPrimitive, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("_outcomeDesc", "_outcomeDesc",fhirprimitive.FHIRPrimitive, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", codeableconcept.CodeableConcept, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, True),
            ("source", "source", AuditEventSource, False, None, True),
            ("subtype", "subtype", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


from . import backboneelement

class AuditEventAgent(backboneelement.BackboneElement):
    """ Actor involved in the event.
    
    An actor taking an active role in the event or activity that is logged.
    """
    
    resource_type = "AuditEventAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altId = None
        
        """ Alternative User identity.
        Type `str`. """
        
        self._altId = None
        
        """ extension for fhir primitive  altId"""
        
        self.location = None
        
        """ Where.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.media = None
        
        """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Human friendly name for the agent.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.network = None
        
        """ Logical network location for application activity.
        Type `AuditEventAgentNetwork` (represented as `dict` in JSON). """
        
        self.policy = None
        
        """ Policy that authorized event.
        List of `str` items. """
        
        self._policy = None
        
        """ extension for fhir primitive  policy"""
        
        self.purposeOfUse = None
        
        """ Reason given for this user.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requestor = None
        
        """ Whether user is initiator.
        Type `bool`. """
        
        self._requestor = None
        
        """ extension for fhir primitive  requestor"""
        
        self.role = None
        
        """ Agent role in the event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ How agent participated.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.who = None
        
        """ Identifier of who.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(AuditEventAgent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AuditEventAgent, self).elementProperties()
        js.extend([
            ("altId", "altId", str, False, None, False),
            ("_altId", "_altId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("media", "media", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("network", "network", AuditEventAgentNetwork, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("_policy", "_policy",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purposeOfUse", "purposeOfUse", codeableconcept.CodeableConcept, True, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("_requestor", "_requestor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """ Logical network location for application activity.
    
    Logical network location for application activity, if the activity has a
    network location.
    """
    
    resource_type = "AuditEventAgentNetwork"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        
        """ Identifier for the network access point of the user device.
        Type `str`. """
        
        self._address = None
        
        """ extension for fhir primitive  address"""
        
        self.type = None
        
        """ The type of network access point.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(AuditEventAgentNetwork, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AuditEventAgentNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("_address", "_address",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class AuditEventEntity(backboneelement.BackboneElement):
    """ Data or objects used.
    
    Specific instances of data or objects that have been accessed.
    """
    
    resource_type = "AuditEventEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Descriptive text.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.detail = None
        
        """ Additional Information about the entity.
        List of `AuditEventEntityDetail` items (represented as `dict` in JSON). """
        
        self.lifecycle = None
        
        """ Life-cycle stage for the entity.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Descriptor for entity.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.query = None
        
        """ Query parameters.
        Type `str`. """
        
        self._query = None
        
        """ extension for fhir primitive  query"""
        
        self.role = None
        
        """ What role the entity played.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.securityLabel = None
        
        """ Security labels on the entity.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of entity involved.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.what = None
        
        """ Specific instance of resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(AuditEventEntity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AuditEventEntity, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("detail", "detail", AuditEventEntityDetail, True, None, False),
            ("lifecycle", "lifecycle", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("query", "query", str, False, None, False),
            ("_query", "_query",fhirprimitive.FHIRPrimitive, False, None, False),
            ("role", "role", coding.Coding, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("what", "what", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class AuditEventEntityDetail(backboneelement.BackboneElement):
    """ Additional Information about the entity.
    
    Tagged value pairs for conveying additional information about the entity.
    """
    
    resource_type = "AuditEventEntityDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        
        """ Name of the property.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.valueBase64Binary = None
        
        """ Property value.
        Type `str`. """
        
        self._valueBase64Binary = None
        
        """ extension for fhir primitive  valueBase64Binary"""
        
        self.valueString = None
        
        """ Property value.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        super(AuditEventEntityDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AuditEventEntityDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class AuditEventSource(backboneelement.BackboneElement):
    """ Audit Event Reporter.
    
    The system that is reporting the event.
    """
    
    resource_type = "AuditEventSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.observer = None
        
        """ The identity of source detecting the event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.site = None
        
        """ Logical source location within the enterprise.
        Type `str`. """
        
        self._site = None
        
        """ extension for fhir primitive  site"""
        
        self.type = None
        
        """ The type of source where event originated.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("observer", "observer", fhirreference.FHIRReference, False, None, True),
            ("site", "site", str, False, None, False),
            ("_site", "_site",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", coding.Coding, True, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import period
from . import fhirprimitive

