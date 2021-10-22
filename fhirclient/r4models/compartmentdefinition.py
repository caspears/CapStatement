#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class CompartmentDefinition(domainresource.DomainResource):
    """ Compartment Definition for a resource.
    
    A compartment definition that defines how resources are accessed on a
    server.
    """
    
    resource_type = "CompartmentDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the compartment definition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.name = None
        
        """ Name for this compartment definition (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this compartment definition is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.resource = None
        
        """ How a resource is related to the compartment.
        List of `CompartmentDefinitionResource` items (represented as `dict` in JSON). """
        
        self.search = None
        
        """ Whether the search syntax is supported.
        Type `bool`. """
        
        self._search = None
        
        """ extension for fhir primitive  search"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.url = None
        
        """ Canonical identifier for this compartment definition, represented
        as a URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the compartment definition.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(CompartmentDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("resource", "resource", CompartmentDefinitionResource, True, None, False),
            ("search", "search", bool, False, None, True),
            ("_search", "_search",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """ How a resource is related to the compartment.
    
    Information about how a resource is related to the compartment.
    """
    
    resource_type = "CompartmentDefinitionResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Name of resource type.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.documentation = None
        
        """ Additional documentation about the resource and compartment.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.param = None
        
        """ Search Parameter Name, or chained parameters.
        List of `str` items. """
        
        self._param = None
        
        """ extension for fhir primitive  param"""
        
        super(CompartmentDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("param", "param", str, True, None, False),
            ("_param", "_param",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import contactdetail
from . import fhirdate
from . import usagecontext
from . import fhirprimitive

