#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource
from . import extensionelement

class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.
    
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """
    
    resource_type = "StructureDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None
        
        """ Whether the structure is abstract.
        Type `bool`. """
        
        self._abstract = None
        
        """ extension for fhir primitive  abstract"""
        
        self.baseDefinition = None
        
        """ Definition that this type is constrained/specialized from.
        Type `str`. """
        
        self._baseDefinition = None
        
        """ extension for fhir primitive  baseDefinition"""
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.context = None
        
        """ If an extension, where it can be used in instances.
        List of `StructureDefinitionContext` items (represented as `dict` in JSON). """
        
        self.contextInvariant = None
        
        """ FHIRPath invariants - when the extension can be used.
        List of `str` items. """
        
        self._contextInvariant = None
        
        """ extension for fhir primitive  contextInvariant"""
        
        self.copyright = None
        
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self._copyright = None
        
        """ extension for fhir primitive  copyright"""
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.derivation = None
        
        """ specialization | constraint - How relates to base definition.
        Type `str`. """
        
        self._derivation = None
        
        """ extension for fhir primitive  derivation"""
        
        self.description = None
        
        """ Natural language description of the structure definition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.differential = None
        
        """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.fhirVersion = None
        
        """ FHIR Version this StructureDefinition targets.
        Type `str`. """
        
        self._fhirVersion = None
        
        """ extension for fhir primitive  fhirVersion"""
        
        self.identifier = None
        
        """ Additional identifier for the structure definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for structure definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.keyword = None
        
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.kind = None
        
        """ primitive-type | complex-type | resource | logical.
        Type `str`. """
        
        self._kind = None
        
        """ extension for fhir primitive  kind"""
        
        self.mapping = None
        
        """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this structure definition (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this structure definition is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.snapshot = None
        
        """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.title = None
        
        """ Name for this structure definition (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.type = None
        
        """ Type defined or constrained by this structure.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.url = None
        
        """ Canonical identifier for this structure definition, represented as
        a URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the structure definition.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(StructureDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, True),
            ("_abstract", "_abstract",extensionelement.ExtensionElement, True, None, False),
            ("baseDefinition", "baseDefinition", str, False, None, False),
            ("_baseDefinition", "_baseDefinition",extensionelement.ExtensionElement, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("context", "context", StructureDefinitionContext, True, None, False),
            ("contextInvariant", "contextInvariant", str, True, None, False),
            ("_contextInvariant", "_contextInvariant",extensionelement.ExtensionElement, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",extensionelement.ExtensionElement, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivation", "derivation", str, False, None, False),
            ("_derivation", "_derivation",extensionelement.ExtensionElement, True, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",extensionelement.ExtensionElement, True, None, False),
            ("differential", "differential", StructureDefinitionDifferential, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",extensionelement.ExtensionElement, True, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("_fhirVersion", "_fhirVersion",extensionelement.ExtensionElement, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("keyword", "keyword", coding.Coding, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind",extensionelement.ExtensionElement, True, None, False),
            ("mapping", "mapping", StructureDefinitionMapping, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",extensionelement.ExtensionElement, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",extensionelement.ExtensionElement, True, None, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",extensionelement.ExtensionElement, True, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",extensionelement.ExtensionElement, True, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",extensionelement.ExtensionElement, True, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url",extensionelement.ExtensionElement, True, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


from . import backboneelement

class StructureDefinitionContext(backboneelement.BackboneElement):
    """ If an extension, where it can be used in instances.
    
    Identifies the types of resource or data type elements to which the
    extension can be applied.
    """
    
    resource_type = "StructureDefinitionContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        
        """ Where the extension can be used in instances.
        Type `str`. """
        
        self._expression = None
        
        """ extension for fhir primitive  expression"""
        
        self.type = None
        
        """ fhirpath | element | extension.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(StructureDefinitionContext, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureDefinitionContext, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, True),
            ("_expression", "_expression",extensionelement.ExtensionElement, True, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.
    
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    
    resource_type = "StructureDefinitionDifferential"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionDifferential, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    resource_type = "StructureDefinitionMapping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        
        """ Versions, Issues, Scope limitations etc..
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.identity = None
        
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self._identity = None
        
        """ extension for fhir primitive  identity"""
        
        self.name = None
        
        """ Names what this mapping refers to.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.uri = None
        
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        self._uri = None
        
        """ extension for fhir primitive  uri"""
        
        super(StructureDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",extensionelement.ExtensionElement, True, None, False),
            ("identity", "identity", str, False, None, True),
            ("_identity", "_identity",extensionelement.ExtensionElement, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
            ("uri", "uri", str, False, None, False),
            ("_uri", "_uri",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.
    
    A snapshot view is expressed in a standalone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    
    resource_type = "StructureDefinitionSnapshot"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionSnapshot, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import elementdefinition
from . import fhirdate
from . import identifier
from . import usagecontext
from . import fhirprimitive

