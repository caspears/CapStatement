#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ResearchElementDefinition(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "ResearchElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        
        """ When the research element definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        
        """ What defines the members of the research element.
        List of `ResearchElementDefinitionCharacteristic` items (represented as `dict` in JSON). """
        
        self.comment = None
        
        """ Used for footnotes or explanatory notes.
        List of `str` items. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
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
        
        """ Natural language description of the research element definition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.editor = None
        
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        
        """ When the research element definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.identifier = None
        
        """ Additional identifier for the research element definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for research element definition (if
        applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        
        """ When the research element definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.library = None
        
        """ Logic used by the ResearchElementDefinition.
        List of `str` items. """
        
        self._library = None
        
        """ extension for fhir primitive  library"""
        
        self.name = None
        
        """ Name for this research element definition (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this research element definition is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
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
        
        self.subjectCodeableConcept = None
        
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subtitle = None
        
        """ Subordinate title of the ResearchElementDefinition.
        Type `str`. """
        
        self._subtitle = None
        
        """ extension for fhir primitive  subtitle"""
        
        self.title = None
        
        """ Name for this research element definition (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.topic = None
        
        """ The category of the ResearchElementDefinition, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ population | exposure | outcome.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.url = None
        
        """ Canonical identifier for this research element definition,
        represented as a URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.usage = None
        
        """ Describes the clinical usage of the ResearchElementDefinition.
        Type `str`. """
        
        self._usage = None
        
        """ extension for fhir primitive  usage"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.variableType = None
        
        """ dichotomous | continuous | descriptive.
        Type `str`. """
        
        self._variableType = None
        
        """ extension for fhir primitive  variableType"""
        
        self.version = None
        
        """ Business version of the research element definition.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(ResearchElementDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("characteristic", "characteristic", ResearchElementDefinitionCharacteristic, True, None, True),
            ("comment", "comment", str, True, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("_library", "_library",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("_shortTitle", "_shortTitle",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("_subtitle", "_subtitle",fhirprimitive.FHIRPrimitive, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("variableType", "variableType", str, False, None, False),
            ("_variableType", "_variableType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the research element.
    
    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    
    resource_type = "ResearchElementDefinitionCharacteristic"
    
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
        
        self.exclude = None
        
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """
        
        self._exclude = None
        
        """ extension for fhir primitive  exclude"""
        
        self.participantEffectiveDateTime = None
        
        """ What time period do participants cover.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.participantEffectiveDescription = None
        
        """ What time period do participants cover.
        Type `str`. """
        
        self._participantEffectiveDescription = None
        
        """ extension for fhir primitive  participantEffectiveDescription"""
        
        self.participantEffectiveDuration = None
        
        """ What time period do participants cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectiveGroupMeasure = None
        
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """
        
        self._participantEffectiveGroupMeasure = None
        
        """ extension for fhir primitive  participantEffectiveGroupMeasure"""
        
        self.participantEffectivePeriod = None
        
        """ What time period do participants cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.participantEffectiveTimeFromStart = None
        
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectiveTiming = None
        
        """ What time period do participants cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.studyEffectiveDateTime = None
        
        """ What time period does the study cover.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.studyEffectiveDescription = None
        
        """ What time period does the study cover.
        Type `str`. """
        
        self._studyEffectiveDescription = None
        
        """ extension for fhir primitive  studyEffectiveDescription"""
        
        self.studyEffectiveDuration = None
        
        """ What time period does the study cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.studyEffectiveGroupMeasure = None
        
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """
        
        self._studyEffectiveGroupMeasure = None
        
        """ extension for fhir primitive  studyEffectiveGroupMeasure"""
        
        self.studyEffectivePeriod = None
        
        """ What time period does the study cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.studyEffectiveTimeFromStart = None
        
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.studyEffectiveTiming = None
        
        """ What time period does the study cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.unitOfMeasure = None
        
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usageContext = None
        
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        super(ResearchElementDefinitionCharacteristic, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("_definitionCanonical", "_definitionCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("exclude", "exclude", bool, False, None, False),
            ("_exclude", "_exclude",fhirprimitive.FHIRPrimitive, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdate.FHIRDate, False, "participantEffective", False),
            ("participantEffectiveDescription", "participantEffectiveDescription", str, False, None, False),
            ("_participantEffectiveDescription", "_participantEffectiveDescription",fhirprimitive.FHIRPrimitive, False, None, False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False),
            ("participantEffectiveGroupMeasure", "participantEffectiveGroupMeasure", str, False, None, False),
            ("_participantEffectiveGroupMeasure", "_participantEffectiveGroupMeasure",fhirprimitive.FHIRPrimitive, False, None, False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False),
            ("participantEffectiveTimeFromStart", "participantEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False),
            ("studyEffectiveDateTime", "studyEffectiveDateTime", fhirdate.FHIRDate, False, "studyEffective", False),
            ("studyEffectiveDescription", "studyEffectiveDescription", str, False, None, False),
            ("_studyEffectiveDescription", "_studyEffectiveDescription",fhirprimitive.FHIRPrimitive, False, None, False),
            ("studyEffectiveDuration", "studyEffectiveDuration", duration.Duration, False, "studyEffective", False),
            ("studyEffectiveGroupMeasure", "studyEffectiveGroupMeasure", str, False, None, False),
            ("_studyEffectiveGroupMeasure", "_studyEffectiveGroupMeasure",fhirprimitive.FHIRPrimitive, False, None, False),
            ("studyEffectivePeriod", "studyEffectivePeriod", period.Period, False, "studyEffective", False),
            ("studyEffectiveTimeFromStart", "studyEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("studyEffectiveTiming", "studyEffectiveTiming", timing.Timing, False, "studyEffective", False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


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
from . import usagecontext
from . import fhirprimitive

