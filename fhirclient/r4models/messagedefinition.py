#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/MessageDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class MessageDefinition(domainresource.DomainResource):
    """ A resource that defines a type of message that can be exchanged between
    systems.
    
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """
    
    resource_type = "MessageDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedResponse = None
        
        """ Responses to this message.
        List of `MessageDefinitionAllowedResponse` items (represented as `dict` in JSON). """
        
        self.base = None
        
        """ Definition this one is based on.
        Type `str`. """
        
        self._base = None
        
        """ extension for fhir primitive  base"""
        
        self.category = None
        
        """ consequence | currency | notification.
        Type `str`. """
        
        self._category = None
        
        """ extension for fhir primitive  category"""
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self._copyright = None
        
        """ extension for fhir primitive  copyright"""
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the message definition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.eventCoding = None
        
        """ Event code  or link to the EventDefinition.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eventUri = None
        
        """ Event code  or link to the EventDefinition.
        Type `str`. """
        
        self._eventUri = None
        
        """ extension for fhir primitive  eventUri"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.focus = None
        
        """ Resource(s) that are the subject of the event.
        List of `MessageDefinitionFocus` items (represented as `dict` in JSON). """
        
        self.graph = None
        
        """ Canonical reference to a GraphDefinition.
        List of `str` items. """
        
        self._graph = None
        
        """ extension for fhir primitive  graph"""
        
        self.identifier = None
        
        """ Primary key for the message definition on a given server.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for message definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this message definition (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.parent = None
        
        """ Protocol/workflow this is part of.
        List of `str` items. """
        
        self._parent = None
        
        """ extension for fhir primitive  parent"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this message definition is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.replaces = None
        
        """ Takes the place of.
        List of `str` items. """
        
        self._replaces = None
        
        """ extension for fhir primitive  replaces"""
        
        self.responseRequired = None
        
        """ always | on-error | never | on-success.
        Type `str`. """
        
        self._responseRequired = None
        
        """ extension for fhir primitive  responseRequired"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.title = None
        
        """ Name for this message definition (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Business Identifier for a given MessageDefinition.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the message definition.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(MessageDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageDefinition, self).elementProperties()
        js.extend([
            ("allowedResponse", "allowedResponse", MessageDefinitionAllowedResponse, True, None, False),
            ("base", "base", str, False, None, False),
            ("_base", "_base",fhirprimitive.FHIRPrimitive, False, None, False),
            ("category", "category", str, False, None, False),
            ("_category", "_category",fhirprimitive.FHIRPrimitive, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("_eventUri", "_eventUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("focus", "focus", MessageDefinitionFocus, True, None, False),
            ("graph", "graph", str, True, None, False),
            ("_graph", "_graph",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("parent", "parent", str, True, None, False),
            ("_parent", "_parent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("_replaces", "_replaces",fhirprimitive.FHIRPrimitive, False, None, False),
            ("responseRequired", "responseRequired", str, False, None, False),
            ("_responseRequired", "_responseRequired",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.
    
    Indicates what types of messages may be sent as an application-level
    response to this message.
    """
    
    resource_type = "MessageDefinitionAllowedResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.message = None
        
        """ Reference to allowed message definition response.
        Type `str`. """
        
        self._message = None
        
        """ extension for fhir primitive  message"""
        
        self.situation = None
        
        """ When should this response be used.
        Type `str`. """
        
        self._situation = None
        
        """ extension for fhir primitive  situation"""
        
        super(MessageDefinitionAllowedResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageDefinitionAllowedResponse, self).elementProperties()
        js.extend([
            ("message", "message", str, False, None, True),
            ("_message", "_message",fhirprimitive.FHIRPrimitive, False, None, False),
            ("situation", "situation", str, False, None, False),
            ("_situation", "_situation",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ Resource(s) that are the subject of the event.
    
    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """
    
    resource_type = "MessageDefinitionFocus"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Type of resource.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.max = None
        
        """ Maximum number of focuses of this type.
        Type `str`. """
        
        self._max = None
        
        """ extension for fhir primitive  max"""
        
        self.min = None
        
        """ Minimum number of focuses of this type.
        Type `int`. """
        
        self._min = None
        
        """ extension for fhir primitive  min"""
        
        self.profile = None
        
        """ Profile that must be adhered to by focus.
        Type `str`. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        super(MessageDefinitionFocus, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageDefinitionFocus, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max",fhirprimitive.FHIRPrimitive, False, None, False),
            ("min", "min", int, False, None, True),
            ("_min", "_min",fhirprimitive.FHIRPrimitive, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import identifier
from . import usagecontext
from . import fhirprimitive

