#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ValueSet) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.
    
    A ValueSet resource instance specifies a set of codes drawn from one or
    more code systems, intended for use in a particular context. Value sets
    link between [CodeSystem](codesystem.html) definitions and their use in
    [coded elements](terminologies.html).
    """
    
    resource_type = "ValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compose = None
        
        """ Content logical definition of the value set (CLD).
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
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
        
        """ Natural language description of the value set.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.expansion = None
        
        """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.identifier = None
        
        """ Additional identifier for the value set (business identifier).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.immutable = None
        
        """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """
        
        self._immutable = None
        
        """ extension for fhir primitive  immutable"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for value set (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this value set (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this value set is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.title = None
        
        """ Name for this value set (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Canonical identifier for this value set, represented as a URI
        (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the value set.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(ValueSet, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("compose", "compose", ValueSetCompose, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("expansion", "expansion", ValueSetExpansion, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("immutable", "immutable", bool, False, None, False),
            ("_immutable", "_immutable",fhirprimitive.FHIRPrimitive, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
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

class ValueSetCompose(backboneelement.BackboneElement):
    """ Content logical definition of the value set (CLD).
    
    A set of criteria that define the contents of the value set by including or
    excluding codes selected from the specified code system(s) that the value
    set draws from. This is also known as the Content Logical Definition (CLD).
    """
    
    resource_type = "ValueSetCompose"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exclude = None
        
        """ Explicitly exclude codes from a code system or other value sets.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.inactive = None
        
        """ Whether inactive codes are in the value set.
        Type `bool`. """
        
        self._inactive = None
        
        """ extension for fhir primitive  inactive"""
        
        self.include = None
        
        """ Include one or more codes from a code system or other value set(s).
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.lockedDate = None
        
        """ Fixed date for references with no specified version (transitive).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ValueSetComposeInclude, True, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("_inactive", "_inactive",fhirprimitive.FHIRPrimitive, False, None, False),
            ("include", "include", ValueSetComposeInclude, True, None, True),
            ("lockedDate", "lockedDate", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ Include one or more codes from a code system or other value set(s).
    """
    
    resource_type = "ValueSetComposeInclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.concept = None
        
        """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        
        self.filter = None
        
        """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        
        self.system = None
        
        """ The system the codes come from.
        Type `str`. """
        
        self._system = None
        
        """ extension for fhir primitive  system"""
        
        self.valueSet = None
        
        """ Select the contents included in this value set.
        List of `str` items. """
        
        self._valueSet = None
        
        """ extension for fhir primitive  valueSet"""
        
        self.version = None
        
        """ Specific version of the code system referred to.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(ValueSetComposeInclude, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("concept", "concept", ValueSetComposeIncludeConcept, True, None, False),
            ("filter", "filter", ValueSetComposeIncludeFilter, True, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueSet", "valueSet", str, True, None, False),
            ("_valueSet", "_valueSet",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ A concept defined in the system.
    
    Specifies a concept to be included or excluded.
    """
    
    resource_type = "ValueSetComposeIncludeConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Code or expression from system.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.designation = None
        
        """ Additional representations for this concept.
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        
        """ Text to display for this code for this value set in this valueset.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for this concept.
    
    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """
    
    resource_type = "ValueSetComposeIncludeConceptDesignation"
    
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
        
        """ Types of uses of designations.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        
        """ The text value for this designation.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(ValueSetComposeIncludeConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetComposeIncludeConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("_language", "_language",fhirprimitive.FHIRPrimitive, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criterion based on the properties
    (including relationships) defined by the system, or on filters defined by
    the system. If multiple filters are specified, they SHALL all be true.
    """
    
    resource_type = "ValueSetComposeIncludeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.op = None
        
        """ = | is-a | descendent-of | is-not-a | regex | in | not-in |
        generalizes | exists.
        Type `str`. """
        
        self._op = None
        
        """ extension for fhir primitive  op"""
        
        self.property = None
        
        """ A property/filter defined by the code system.
        Type `str`. """
        
        self._property = None
        
        """ extension for fhir primitive  property"""
        
        self.value = None
        
        """ Code from the system, or regex criteria, or boolean value for
        exists.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("op", "op", str, False, None, True),
            ("_op", "_op",fhirprimitive.FHIRPrimitive, False, None, False),
            ("property", "property", str, False, None, True),
            ("_property", "_property",fhirprimitive.FHIRPrimitive, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ValueSetExpansion(backboneelement.BackboneElement):
    """ Used when the value set is "expanded".
    
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    
    resource_type = "ValueSetExpansion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contains = None
        
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Identifies the value set expansion (business identifier).
        Type `str`. """
        
        self._identifier = None
        
        """ extension for fhir primitive  identifier"""
        
        self.offset = None
        
        """ Offset at which this resource starts.
        Type `int`. """
        
        self._offset = None
        
        """ extension for fhir primitive  offset"""
        
        self.parameter = None
        
        """ Parameter that controlled the expansion process.
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """
        
        self.timestamp = None
        
        """ Time ValueSet expansion happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.total = None
        
        """ Total number of codes in the expansion.
        Type `int`. """
        
        self._total = None
        
        """ extension for fhir primitive  total"""
        
        super(ValueSetExpansion, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("identifier", "identifier", str, False, None, False),
            ("_identifier", "_identifier",fhirprimitive.FHIRPrimitive, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("_offset", "_offset",fhirprimitive.FHIRPrimitive, False, None, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True, None, False),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, True),
            ("total", "total", int, False, None, False),
            ("_total", "_total",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ Codes in the value set.
    
    The codes that are contained in the value set expansion.
    """
    
    resource_type = "ValueSetExpansionContains"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None
        
        """ If user cannot select this entry.
        Type `bool`. """
        
        self._abstract = None
        
        """ extension for fhir primitive  abstract"""
        
        self.code = None
        
        """ Code - if blank, this is not a selectable code.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.contains = None
        
        """ Codes contained under this entry.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.designation = None
        
        """ Additional representations for this item.
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        
        """ User display for the concept.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.inactive = None
        
        """ If concept is inactive in the code system.
        Type `bool`. """
        
        self._inactive = None
        
        """ extension for fhir primitive  inactive"""
        
        self.system = None
        
        """ System value for the code.
        Type `str`. """
        
        self._system = None
        
        """ extension for fhir primitive  system"""
        
        self.version = None
        
        """ Version in which this code/display is defined.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(ValueSetExpansionContains, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, False),
            ("_abstract", "_abstract",fhirprimitive.FHIRPrimitive, False, None, False),
            ("code", "code", str, False, None, False),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("_inactive", "_inactive",fhirprimitive.FHIRPrimitive, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """ Parameter that controlled the expansion process.
    
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    
    resource_type = "ValueSetExpansionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        
        """ Name as assigned by the client or server.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.valueBoolean = None
        
        """ Value of the named parameter.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCode = None
        
        """ Value of the named parameter.
        Type `str`. """
        
        self._valueCode = None
        
        """ extension for fhir primitive  valueCode"""
        
        self.valueDateTime = None
        
        """ Value of the named parameter.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        
        """ Value of the named parameter.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueInteger = None
        
        """ Value of the named parameter.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueString = None
        
        """ Value of the named parameter.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueUri = None
        
        """ Value of the named parameter.
        Type `str`. """
        
        self._valueUri = None
        
        """ extension for fhir primitive  valueUri"""
        
        super(ValueSetExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("_valueCode", "_valueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("_valueUri", "_valueUri",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import identifier
from . import usagecontext
from . import fhirprimitive

