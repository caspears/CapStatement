#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.
    
    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """
    
    resource_type = "ConceptMap"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        """ Natural language description of the concept map.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.group = None
        
        """ Same source and target systems.
        List of `ConceptMapGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for concept map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this concept map (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this concept map is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.sourceCanonical = None
        
        """ The source value set that contains the concepts that are being
        mapped.
        Type `str`. """
        
        self._sourceCanonical = None
        
        """ extension for fhir primitive  sourceCanonical"""
        
        self.sourceUri = None
        
        """ The source value set that contains the concepts that are being
        mapped.
        Type `str`. """
        
        self._sourceUri = None
        
        """ extension for fhir primitive  sourceUri"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.targetCanonical = None
        
        """ The target value set which provides context for the mappings.
        Type `str`. """
        
        self._targetCanonical = None
        
        """ extension for fhir primitive  targetCanonical"""
        
        self.targetUri = None
        
        """ The target value set which provides context for the mappings.
        Type `str`. """
        
        self._targetUri = None
        
        """ extension for fhir primitive  targetUri"""
        
        self.title = None
        
        """ Name for this concept map (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Canonical identifier for this concept map, represented as a URI
        (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the concept map.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(ConceptMap, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("group", "group", ConceptMapGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sourceCanonical", "sourceCanonical", str, False, "source", False),
            ("_sourceCanonical", "_sourceCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sourceUri", "sourceUri", str, False, "source", False),
            ("_sourceUri", "_sourceUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("targetCanonical", "targetCanonical", str, False, "target", False),
            ("_targetCanonical", "_targetCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("targetUri", "targetUri", str, False, "target", False),
            ("_targetUri", "_targetUri",fhirprimitive.FHIRPrimitive, False, None, False),
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

class ConceptMapGroup(backboneelement.BackboneElement):
    """ Same source and target systems.
    
    A group of mappings that all have the same source and target system.
    """
    
    resource_type = "ConceptMapGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        
        """ Mappings for a concept from the source set.
        List of `ConceptMapGroupElement` items (represented as `dict` in JSON). """
        
        self.source = None
        
        """ Source system where concepts to be mapped are defined.
        Type `str`. """
        
        self._source = None
        
        """ extension for fhir primitive  source"""
        
        self.sourceVersion = None
        
        """ Specific version of the  code system.
        Type `str`. """
        
        self._sourceVersion = None
        
        """ extension for fhir primitive  sourceVersion"""
        
        self.target = None
        
        """ Target system that the concepts are to be mapped to.
        Type `str`. """
        
        self._target = None
        
        """ extension for fhir primitive  target"""
        
        self.targetVersion = None
        
        """ Specific version of the  code system.
        Type `str`. """
        
        self._targetVersion = None
        
        """ extension for fhir primitive  targetVersion"""
        
        self.unmapped = None
        
        """ What to do when there is no mapping for the source concept.
        Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON). """
        
        super(ConceptMapGroup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("element", "element", ConceptMapGroupElement, True, None, True),
            ("source", "source", str, False, None, False),
            ("_source", "_source",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sourceVersion", "sourceVersion", str, False, None, False),
            ("_sourceVersion", "_sourceVersion",fhirprimitive.FHIRPrimitive, False, None, False),
            ("target", "target", str, False, None, False),
            ("_target", "_target",fhirprimitive.FHIRPrimitive, False, None, False),
            ("targetVersion", "targetVersion", str, False, None, False),
            ("_targetVersion", "_targetVersion",fhirprimitive.FHIRPrimitive, False, None, False),
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, False, None, False),
        ])
        return js


class ConceptMapGroupElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.
    
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    
    resource_type = "ConceptMapGroupElement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Identifies element being mapped.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.display = None
        
        """ Display for the code.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.target = None
        
        """ Concept in target system for element.
        List of `ConceptMapGroupElementTarget` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("target", "target", ConceptMapGroupElementTarget, True, None, False),
        ])
        return js


class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.
    
    A concept from the target value set that this concept maps to.
    """
    
    resource_type = "ConceptMapGroupElementTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Code that identifies the target element.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.comment = None
        
        """ Description of status/issues in mapping.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.dependsOn = None
        
        """ Other elements required for this mapping (from context).
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        self.display = None
        
        """ Display for the code.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.equivalence = None
        
        """ relatedto | equivalent | equal | wider | subsumes | narrower |
        specializes | inexact | unmatched | disjoint.
        Type `str`. """
        
        self._equivalence = None
        
        """ extension for fhir primitive  equivalence"""
        
        self.product = None
        
        """ Other concepts that this mapping also produces.
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElementTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, True, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("equivalence", "equivalence", str, False, None, True),
            ("_equivalence", "_equivalence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("product", "product", ConceptMapGroupElementTargetDependsOn, True, None, False),
        ])
        return js


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).
    
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    
    resource_type = "ConceptMapGroupElementTargetDependsOn"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.display = None
        
        """ Display for the code (if value is a code).
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.property = None
        
        """ Reference to property mapping depends on.
        Type `str`. """
        
        self._property = None
        
        """ extension for fhir primitive  property"""
        
        self.system = None
        
        """ Code System (if necessary).
        Type `str`. """
        
        self._system = None
        
        """ extension for fhir primitive  system"""
        
        self.value = None
        
        """ Value of the referenced element.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(ConceptMapGroupElementTargetDependsOn, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("property", "property", str, False, None, True),
            ("_property", "_property",fhirprimitive.FHIRPrimitive, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system",fhirprimitive.FHIRPrimitive, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """ What to do when there is no mapping for the source concept.
    
    What to do when there is no mapping for the source concept. "Unmapped" does
    not include codes that are unamatched, and the unmapped element is ignored
    in a code is specified to have equivalence = unmatched.
    """
    
    resource_type = "ConceptMapGroupUnmapped"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Fixed code when mode = fixed.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.display = None
        
        """ Display for the code.
        Type `str`. """
        
        self._display = None
        
        """ extension for fhir primitive  display"""
        
        self.mode = None
        
        """ provided | fixed | other-map.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.url = None
        
        """ canonical reference to an additional ConceptMap to use for mapping
        if the source concept is unmapped.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        super(ConceptMapGroupUnmapped, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code",fhirprimitive.FHIRPrimitive, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display",fhirprimitive.FHIRPrimitive, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import identifier
from . import usagecontext
from . import fhirprimitive

