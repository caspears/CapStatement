#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Library) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Library(domainresource.DomainResource):
    """ Represents a library of quality improvement components.
    
    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as well
    as to describe a collection of knowledge assets.
    """
    
    resource_type = "Library"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        
        """ When the library was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.content = None
        
        """ Contents of the library, either embedded or referenced.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.copyright = None
        
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self._copyright = None
        
        """ extension for fhir primitive  copyright"""
        
        self.dataRequirement = None
        
        """ What data is referenced by this library.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the library.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.editor = None
        
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        
        """ When the library is expected to be used.
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
        
        """ Additional identifier for the library.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for library (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        
        """ When the library was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        
        """ Name for this library (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.parameter = None
        
        """ Parameters defined by the library.
        List of `ParameterDefinition` items (represented as `dict` in JSON). """
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this library is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.relatedArtifact = None
        
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subjectCodeableConcept = None
        
        """ Type of individual the library content is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        
        """ Type of individual the library content is focused on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subtitle = None
        
        """ Subordinate title of the library.
        Type `str`. """
        
        self._subtitle = None
        
        """ extension for fhir primitive  subtitle"""
        
        self.title = None
        
        """ Name for this library (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.topic = None
        
        """ E.g. Education, Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ logic-library | model-definition | asset-collection | module-
        definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.url = None
        
        """ Canonical identifier for this library, represented as a URI
        (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.usage = None
        
        """ Describes the clinical usage of the library.
        Type `str`. """
        
        self._usage = None
        
        """ extension for fhir primitive  usage"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the library.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(Library, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Library, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("content", "content", attachment.Attachment, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
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
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("_subtitle", "_subtitle",fhirprimitive.FHIRPrimitive, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import fhirdate
from . import fhirreference
from . import identifier
from . import parameterdefinition
from . import period
from . import relatedartifact
from . import usagecontext
from . import fhirprimitive

