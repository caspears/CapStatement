#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class EvidenceVariable(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    
    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "EvidenceVariable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        
        """ When the evidence variable was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        
        """ What defines the members of the evidence element.
        List of `EvidenceVariableCharacteristic` items (represented as `dict` in JSON). """
        
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
        
        """ Natural language description of the evidence variable.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.editor = None
        
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        
        """ When the evidence variable is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Additional identifier for the evidence variable.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for evidence variable (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        
        """ When the evidence variable was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        
        """ Name for this evidence variable (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.note = None
        
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.relatedArtifact = None
        
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.shortTitle = None
        
        """ Title for use in informal contexts.
        Type `str`. """
        
        self._shortTitle = None
        
        """ extension for fhir primitive  shortTitle"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subtitle = None
        
        """ Subordinate title of the EvidenceVariable.
        Type `str`. """
        
        self._subtitle = None
        
        """ extension for fhir primitive  subtitle"""
        
        self.title = None
        
        """ Name for this evidence variable (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.topic = None
        
        """ The category of the EvidenceVariable, such as Education, Treatment,
        Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ dichotomous | continuous | descriptive.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.url = None
        
        """ Canonical identifier for this evidence variable, represented as a
        URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the evidence variable.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(EvidenceVariable, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, True, None, True),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("_shortTitle", "_shortTitle",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("_subtitle", "_subtitle",fhirprimitive.FHIRPrimitive, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the evidence element.
    
    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """
    
    resource_type = "EvidenceVariableCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definitionCanonical = None
        
        """ What code or expression defines members?.
        Type `str`. """
        
        self._definitionCanonical = None
        
        """ extension for fhir primitive  definitionCanonical"""
        
        self.definitionCodeableConcept = None
        
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definitionDataRequirement = None
        
        """ What code or expression defines members?.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.definitionExpression = None
        
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.definitionReference = None
        
        """ What code or expression defines members?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definitionTriggerDefinition = None
        
        """ What code or expression defines members?.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Natural language description of the characteristic.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.exclude = None
        
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """
        
        self._exclude = None
        
        """ extension for fhir primitive  exclude"""
        
        self.groupMeasure = None
        
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """
        
        self._groupMeasure = None
        
        """ extension for fhir primitive  groupMeasure"""
        
        self.participantEffectiveDateTime = None
        
        """ What time period do participants cover.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.participantEffectiveDuration = None
        
        """ What time period do participants cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectivePeriod = None
        
        """ What time period do participants cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.participantEffectiveTiming = None
        
        """ What time period do participants cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.timeFromStart = None
        
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.usageContext = None
        
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        super(EvidenceVariableCharacteristic, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("_definitionCanonical", "_definitionCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("definitionReference", "definitionReference", fhirreference.FHIRReference, False, "definition", True),
            ("definitionTriggerDefinition", "definitionTriggerDefinition", triggerdefinition.TriggerDefinition, False, "definition", True),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("_exclude", "_exclude",fhirprimitive.FHIRPrimitive, False, None, False),
            ("groupMeasure", "groupMeasure", str, False, None, False),
            ("_groupMeasure", "_groupMeasure",fhirprimitive.FHIRPrimitive, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdate.FHIRDate, False, "participantEffective", False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False),
            ("timeFromStart", "timeFromStart", duration.Duration, False, None, False),
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import timing
from . import triggerdefinition
from . import usagecontext
from . import fhirprimitive

