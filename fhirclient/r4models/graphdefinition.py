#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/GraphDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class GraphDefinition(domainresource.DomainResource):
    """ Definition of a graph of resources.
    
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """
    
    resource_type = "GraphDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the graph definition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for graph definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.link = None
        
        """ Links this graph makes rules about.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this graph definition (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.profile = None
        
        """ Profile on base resource.
        Type `str`. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this graph definition is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.start = None
        
        """ Type of resource at which the graph starts.
        Type `str`. """
        
        self._start = None
        
        """ extension for fhir primitive  start"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.url = None
        
        """ Canonical identifier for this graph definition, represented as a
        URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the graph definition.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(GraphDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("start", "start", str, False, None, True),
            ("_start", "_start",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class GraphDefinitionLink(backboneelement.BackboneElement):
    """ Links this graph makes rules about.
    """
    
    resource_type = "GraphDefinitionLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Why this link is specified.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.max = None
        
        """ Maximum occurrences for this link.
        Type `str`. """
        
        self._max = None
        
        """ extension for fhir primitive  max"""
        
        self.min = None
        
        """ Minimum occurrences for this link.
        Type `int`. """
        
        self._min = None
        
        """ extension for fhir primitive  min"""
        
        self.path = None
        
        """ Path in the resource that contains the link.
        Type `str`. """
        
        self._path = None
        
        """ extension for fhir primitive  path"""
        
        self.sliceName = None
        
        """ Which slice (if profiled).
        Type `str`. """
        
        self._sliceName = None
        
        """ extension for fhir primitive  sliceName"""
        
        self.target = None
        
        """ Potential target for the link.
        List of `GraphDefinitionLinkTarget` items (represented as `dict` in JSON). """
        
        super(GraphDefinitionLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max",fhirprimitive.FHIRPrimitive, False, None, False),
            ("min", "min", int, False, None, False),
            ("_min", "_min",fhirprimitive.FHIRPrimitive, False, None, False),
            ("path", "path", str, False, None, False),
            ("_path", "_path",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("_sliceName", "_sliceName",fhirprimitive.FHIRPrimitive, False, None, False),
            ("target", "target", GraphDefinitionLinkTarget, True, None, False),
        ])
        return js


class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """ Potential target for the link.
    """
    
    resource_type = "GraphDefinitionLinkTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        
        """ Compartment Consistency Rules.
        List of `GraphDefinitionLinkTargetCompartment` items (represented as `dict` in JSON). """
        
        self.link = None
        
        """ Additional links from target resource.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
        self.params = None
        
        """ Criteria for reverse lookup.
        Type `str`. """
        
        self._params = None
        
        """ extension for fhir primitive  params"""
        
        self.profile = None
        
        """ Profile for the target resource.
        Type `str`. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        self.type = None
        
        """ Type of resource this link refers to.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(GraphDefinitionLinkTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend([
            ("compartment", "compartment", GraphDefinitionLinkTargetCompartment, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("params", "params", str, False, None, False),
            ("_params", "_params",fhirprimitive.FHIRPrimitive, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """ Compartment Consistency Rules.
    """
    
    resource_type = "GraphDefinitionLinkTargetCompartment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Identifies the compartment.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.description = None
        
        """ Documentation for FHIRPath expression.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.expression = None
        
        """ Custom rule, as a FHIRPath expression.
        Type `str`. """
        
        self._expression = None
        
        """ extension for fhir primitive  expression"""
        
        self.rule = None
        
        """ identical | matching | different | custom.
        Type `str`. """
        
        self._rule = None
        
        """ extension for fhir primitive  rule"""
        
        self.use = None
        
        """ condition | requirement.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        super(GraphDefinitionLinkTargetCompartment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression",fhirprimitive.FHIRPrimitive, False, None, False),
            ("rule", "rule", str, False, None, True),
            ("_rule", "_rule",fhirprimitive.FHIRPrimitive, False, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import usagecontext
from . import fhirprimitive

