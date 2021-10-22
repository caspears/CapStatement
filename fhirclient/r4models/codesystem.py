#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/CodeSystem) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class CodeSystem(domainresource.DomainResource):
    """ Declares the existence of and describes a code system or code system
    supplement.
    
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """
    
    resource_type = "CodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.caseSensitive = None
        
        """ If code comparison is case sensitive.
        Type `bool`. """
        
        self._caseSensitive = None
        
        """ extension for fhir primitive  caseSensitive"""
        
        self.compositional = None
        
        """ If code system defines a compositional grammar.
        Type `bool`. """
        
        self._compositional = None
        
        """ extension for fhir primitive  compositional"""
        
        self.concept = None
        
        """ Concepts in the code system.
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.content = None
        
        """ not-present | example | fragment | complete | supplement.
        Type `str`. """
        
        self._content = None
        
        """ extension for fhir primitive  content"""
        
        self.copyright = None
        
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self._copyright = None
        
        """ extension for fhir primitive  copyright"""
        
        self.count = None
        
        """ Total concepts in the code system.
        Type `int`. """
        
        self._count = None
        
        """ extension for fhir primitive  count"""
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the code system.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.filter = None
        
        """ Filter that can be used in a value set.
        List of `CodeSystemFilter` items (represented as `dict` in JSON). """
        
        self.hierarchyMeaning = None
        
        """ grouped-by | is-a | part-of | classified-with.
        Type `str`. """
        
        self._hierarchyMeaning = None
        
        """ extension for fhir primitive  hierarchyMeaning"""
        
        self.identifier = None
        
        """ Additional identifier for the code system (business identifier).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for code system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this code system (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.property = None
        
        """ Additional information supplied about each concept.
        List of `CodeSystemProperty` items (represented as `dict` in JSON). """
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this code system is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.supplements = None
        
        """ Canonical URL of Code System this adds designations and properties
        to.
        Type `str`. """
        
        self._supplements = None
        
        """ extension for fhir primitive  supplements"""
        
        self.title = None
        
        """ Name for this code system (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Canonical identifier for this code system, represented as a URI
        (globally unique) (Coding.system).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.valueSet = None
        
        """ Canonical reference to the value set with entire code system.
        Type `str`. """
        
        self._valueSet = None
        
        """ extension for fhir primitive  valueSet"""
        
        self.version = None
        
        """ Business version of the code system (Coding.version).
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        self.versionNeeded = None
        
        """ If definitions are not stable.
        Type `bool`. """
        
        self._versionNeeded = None
        
        """ extension for fhir primitive  versionNeeded"""
        
        super(CodeSystem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystem, self).elementProperties()
        js.extend([
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("_caseSensitive", "_caseSensitive",fhirprimitive.FHIRPrimitive, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("_compositional", "_compositional",fhirprimitive.FHIRPrimitive, False, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("content", "content", str, False, None, True),
            ("_content", "_content",fhirprimitive.FHIRPrimitive, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("count", "count", int, False, None, False),
            ("_count", "_count",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("filter", "filter", CodeSystemFilter, True, None, False),
            ("hierarchyMeaning", "hierarchyMeaning", str, False, None, False),
            ("_hierarchyMeaning", "_hierarchyMeaning",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("property", "property", CodeSystemProperty, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("supplements", "supplements", str, False, None, False),
            ("_supplements", "_supplements",fhirprimitive.FHIRPrimitive, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("_valueSet", "_valueSet",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
            ("versionNeeded", "versionNeeded", bool, False, None, False),
            ("_versionNeeded", "_versionNeeded",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class CodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.
    
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """
    
    resource_type = "CodeSystemConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Code that identifies concept.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.concept = None
        
        """ Child Concepts (is-a/contains/categorizes).
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        
        self.definition = None
        
        """ Formal definition.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.designation = None
        
        """ Additional representations for the concept.
        List of `CodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        
        """ Text to display to the user.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.property = None
        
        """ Property value for the concept.
        List of `CodeSystemConceptProperty` items (represented as `dict` in JSON). """
        
        super(CodeSystemConcept, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("designation", "designation", CodeSystemConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("property", "property", CodeSystemConceptProperty, True, None, False),
        ])
        return js


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.
    
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    
    resource_type = "CodeSystemConceptDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        
        """ Human language of the designation.
        Type `str`. """
        
        self._language = None
        
        """ extension for fhir primitive  language"""
        
        self.use = None
        
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        
        """ The text value for this designation.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(CodeSystemConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("_language", "_language",fhirprimitive.FHIRPrimitive, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """ Property value for the concept.
    
    A property value for this concept.
    """
    
    resource_type = "CodeSystemConceptProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Reference to CodeSystem.property.code.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.valueBoolean = None
        
        """ Value of the property for this concept.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCode = None
        
        """ Value of the property for this concept.
        Type `str`. """
        
        self._valueCode = None
        
        """ extension for fhir primitive  valueCode"""
        
        self.valueCoding = None
        
        """ Value of the property for this concept.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        
        """ Value of the property for this concept.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        
        """ Value of the property for this concept.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueInteger = None
        
        """ Value of the property for this concept.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueString = None
        
        """ Value of the property for this concept.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        super(CodeSystemConceptProperty, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemConceptProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class CodeSystemFilter(backboneelement.BackboneElement):
    """ Filter that can be used in a value set.
    
    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """
    
    resource_type = "CodeSystemFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Code that identifies the filter.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.description = None
        
        """ How or why the filter is used.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.operator = None
        
        """ Operators that can be used with filter.
        List of `str` items. """
        
        self._operator = None
        
        """ extension for fhir primitive  operator"""
        
        self.value = None
        
        """ What to use for the value.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(CodeSystemFilter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("operator", "operator", str, True, None, True),
            ("_operator", "_operator",fhirprimitive.FHIRPrimitive, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class CodeSystemProperty(backboneelement.BackboneElement):
    """ Additional information supplied about each concept.
    
    A property defines an additional slot through which additional information
    can be provided about a concept.
    """
    
    resource_type = "CodeSystemProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Identifies the property on the concepts, and when referred to in
        operations.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.description = None
        
        """ Why the property is defined, and/or what it conveys.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.type = None
        
        """ code | Coding | string | integer | boolean | dateTime | decimal.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.uri = None
        
        """ Formal identifier for the property.
        Type `str`. """
        
        self._uri = None
        
        """ extension for fhir primitive  uri"""
        
        super(CodeSystemProperty, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CodeSystemProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("uri", "uri", str, False, None, False),
            ("_uri", "_uri",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import identifier
from . import usagecontext
from . import fhirprimitive

