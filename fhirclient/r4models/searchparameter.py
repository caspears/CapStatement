#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.
    
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    
    resource_type = "SearchParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.base = None
        
        """ The resource type(s) this search parameter applies to.
        List of `str` items. """
        
        self._base = None
        
        """ extension for fhir primitive  base"""
        
        self.chain = None
        
        """ Chained names supported.
        List of `str` items. """
        
        self._chain = None
        
        """ extension for fhir primitive  chain"""
        
        self.code = None
        
        """ Code used in URL.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.comparator = None
        
        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
        List of `str` items. """
        
        self._comparator = None
        
        """ extension for fhir primitive  comparator"""
        
        self.component = None
        
        """ For Composite resources to define the parts.
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.derivedFrom = None
        
        """ Original definition for the search parameter.
        Type `str`. """
        
        self._derivedFrom = None
        
        """ extension for fhir primitive  derivedFrom"""
        
        self.description = None
        
        """ Natural language description of the search parameter.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.expression = None
        
        """ FHIRPath expression that extracts the values.
        Type `str`. """
        
        self._expression = None
        
        """ extension for fhir primitive  expression"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for search parameter (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.modifier = None
        
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type | identifier | ofType.
        List of `str` items. """
        
        self._modifier = None
        
        """ extension for fhir primitive  modifier"""
        
        self.multipleAnd = None
        
        """ Allow multiple parameters (and).
        Type `bool`. """
        
        self._multipleAnd = None
        
        """ extension for fhir primitive  multipleAnd"""
        
        self.multipleOr = None
        
        """ Allow multiple values per parameter (or).
        Type `bool`. """
        
        self._multipleOr = None
        
        """ extension for fhir primitive  multipleOr"""
        
        self.name = None
        
        """ Name for this search parameter (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this search parameter is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.target = None
        
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self._target = None
        
        """ extension for fhir primitive  target"""
        
        self.type = None
        
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.url = None
        
        """ Canonical identifier for this search parameter, represented as a
        URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the search parameter.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        self.xpath = None
        
        """ XPath that extracts the values.
        Type `str`. """
        
        self._xpath = None
        
        """ extension for fhir primitive  xpath"""
        
        self.xpathUsage = None
        
        """ normal | phonetic | nearby | distance | other.
        Type `str`. """
        
        self._xpathUsage = None
        
        """ extension for fhir primitive  xpathUsage"""
        
        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", str, True, None, True),
            ("_base", "_base",fhirprimitive.FHIRPrimitive, False, None, False),
            ("chain", "chain", str, True, None, False),
            ("_chain", "_chain",fhirprimitive.FHIRPrimitive, False, None, False),
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("comparator", "comparator", str, True, None, False),
            ("_comparator", "_comparator",fhirprimitive.FHIRPrimitive, False, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", str, False, None, False),
            ("_derivedFrom", "_derivedFrom",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, True),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression",fhirprimitive.FHIRPrimitive, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("modifier", "modifier", str, True, None, False),
            ("_modifier", "_modifier",fhirprimitive.FHIRPrimitive, False, None, False),
            ("multipleAnd", "multipleAnd", bool, False, None, False),
            ("_multipleAnd", "_multipleAnd",fhirprimitive.FHIRPrimitive, False, None, False),
            ("multipleOr", "multipleOr", bool, False, None, False),
            ("_multipleOr", "_multipleOr",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("target", "target", str, True, None, False),
            ("_target", "_target",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("_xpath", "_xpath",fhirprimitive.FHIRPrimitive, False, None, False),
            ("xpathUsage", "xpathUsage", str, False, None, False),
            ("_xpathUsage", "_xpathUsage",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.
    
    Used to define the parts of a composite search parameter.
    """
    
    resource_type = "SearchParameterComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        
        """ Defines how the part works.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.expression = None
        
        """ Subexpression relative to main expression.
        Type `str`. """
        
        self._expression = None
        
        """ extension for fhir primitive  expression"""
        
        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("_definition", "_definition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("expression", "expression", str, False, None, True),
            ("_expression", "_expression",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import usagecontext
from . import fhirprimitive

