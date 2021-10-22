#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Subscription) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Subscription(domainresource.DomainResource):
    """ Server push subscription criteria.
    
    The subscription resource is used to define a push-based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """
    
    resource_type = "Subscription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.channel = None
        
        """ The channel on which to report matches to the criteria.
        Type `SubscriptionChannel` (represented as `dict` in JSON). """
        
        self.contact = None
        
        """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.criteria = None
        
        """ Rule for server push.
        Type `str`. """
        
        self._criteria = None
        
        """ extension for fhir primitive  criteria"""
        
        self.end = None
        
        """ When to automatically delete the subscription.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.error = None
        
        """ Latest error note.
        Type `str`. """
        
        self._error = None
        
        """ extension for fhir primitive  error"""
        
        self.reason = None
        
        """ Description of why this subscription was created.
        Type `str`. """
        
        self._reason = None
        
        """ extension for fhir primitive  reason"""
        
        self.status = None
        
        """ requested | active | error | off.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(Subscription, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Subscription, self).elementProperties()
        js.extend([
            ("channel", "channel", SubscriptionChannel, False, None, True),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("criteria", "criteria", str, False, None, True),
            ("_criteria", "_criteria",fhirprimitive.FHIRPrimitive, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("error", "error", str, False, None, False),
            ("_error", "_error",fhirprimitive.FHIRPrimitive, False, None, False),
            ("reason", "reason", str, False, None, True),
            ("_reason", "_reason",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class SubscriptionChannel(backboneelement.BackboneElement):
    """ The channel on which to report matches to the criteria.
    
    Details where to send notifications when resources are received that meet
    the criteria.
    """
    
    resource_type = "SubscriptionChannel"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        
        """ Where the channel points to.
        Type `str`. """
        
        self._endpoint = None
        
        """ extension for fhir primitive  endpoint"""
        
        self.header = None
        
        """ Usage depends on the channel type.
        List of `str` items. """
        
        self._header = None
        
        """ extension for fhir primitive  header"""
        
        self.payload = None
        
        """ MIME type to send, or omit for no payload.
        Type `str`. """
        
        self._payload = None
        
        """ extension for fhir primitive  payload"""
        
        self.type = None
        
        """ rest-hook | websocket | email | sms | message.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(SubscriptionChannel, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubscriptionChannel, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, False),
            ("_endpoint", "_endpoint",fhirprimitive.FHIRPrimitive, False, None, False),
            ("header", "header", str, True, None, False),
            ("_header", "_header",fhirprimitive.FHIRPrimitive, False, None, False),
            ("payload", "payload", str, False, None, False),
            ("_payload", "_payload",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import contactpoint
from . import fhirdate
from . import fhirprimitive

