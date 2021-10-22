#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class RiskEvidenceSynthesis(domainresource.DomainResource):
    """ A quantified estimate of risk based on a body of evidence.
    
    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """
    
    resource_type = "RiskEvidenceSynthesis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        
        """ When the risk evidence synthesis was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.certainty = None
        
        """ How certain is the risk.
        List of `RiskEvidenceSynthesisCertainty` items (represented as `dict` in JSON). """
        
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
        
        """ Natural language description of the risk evidence synthesis.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.editor = None
        
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        
        """ When the risk evidence synthesis is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.exposure = None
        
        """ What exposure?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Additional identifier for the risk evidence synthesis.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for risk evidence synthesis (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        
        """ When the risk evidence synthesis was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        
        """ Name for this risk evidence synthesis (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.note = None
        
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        
        """ What outcome?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.population = None
        
        """ What population?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.riskEstimate = None
        
        """ What was the estimated risk.
        Type `RiskEvidenceSynthesisRiskEstimate` (represented as `dict` in JSON). """
        
        self.sampleSize = None
        
        """ What sample size was involved?.
        Type `RiskEvidenceSynthesisSampleSize` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.studyType = None
        
        """ Type of study.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.synthesisType = None
        
        """ Type of synthesis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.title = None
        
        """ Name for this risk evidence synthesis (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.topic = None
        
        """ The category of the EffectEvidenceSynthesis, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.url = None
        
        """ Canonical identifier for this risk evidence synthesis, represented
        as a URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the risk evidence synthesis.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(RiskEvidenceSynthesis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("certainty", "certainty", RiskEvidenceSynthesisCertainty, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, True),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("riskEstimate", "riskEstimate", RiskEvidenceSynthesisRiskEstimate, False, None, False),
            ("sampleSize", "sampleSize", RiskEvidenceSynthesisSampleSize, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False),
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ How certain is the risk.
    
    A description of the certainty of the risk estimate.
    """
    
    resource_type = "RiskEvidenceSynthesisCertainty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.certaintySubcomponent = None
        
        """ A component that contributes to the overall certainty.
        List of `RiskEvidenceSynthesisCertaintyCertaintySubcomponent` items (represented as `dict` in JSON). """
        
        self.note = None
        
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.rating = None
        
        """ Certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisCertainty, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("certaintySubcomponent", "certaintySubcomponent", RiskEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(backboneelement.BackboneElement):
    """ A component that contributes to the overall certainty.
    
    A description of a component of the overall certainty.
    """
    
    resource_type = "RiskEvidenceSynthesisCertaintyCertaintySubcomponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.note = None
        
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.rating = None
        
        """ Subcomponent certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of subcomponent of certainty rating.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class RiskEvidenceSynthesisRiskEstimate(backboneelement.BackboneElement):
    """ What was the estimated risk.
    
    The estimated risk of the outcome.
    """
    
    resource_type = "RiskEvidenceSynthesisRiskEstimate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.denominatorCount = None
        
        """ Sample size for group measured.
        Type `int`. """
        
        self._denominatorCount = None
        
        """ extension for fhir primitive  denominatorCount"""
        
        self.description = None
        
        """ Description of risk estimate.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.numeratorCount = None
        
        """ Number with the outcome.
        Type `int`. """
        
        self._numeratorCount = None
        
        """ extension for fhir primitive  numeratorCount"""
        
        self.precisionEstimate = None
        
        """ How precise the estimate is.
        List of `RiskEvidenceSynthesisRiskEstimatePrecisionEstimate` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of risk estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitOfMeasure = None
        
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        
        """ Point estimate.
        Type `float`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(RiskEvidenceSynthesisRiskEstimate, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimate, self).elementProperties()
        js.extend([
            ("denominatorCount", "denominatorCount", int, False, None, False),
            ("_denominatorCount", "_denominatorCount",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("numeratorCount", "numeratorCount", int, False, None, False),
            ("_numeratorCount", "_numeratorCount",fhirprimitive.FHIRPrimitive, False, None, False),
            ("precisionEstimate", "precisionEstimate", RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(backboneelement.BackboneElement):
    """ How precise the estimate is.
    
    A description of the precision of the estimate for the effect.
    """
    
    resource_type = "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.from_fhir = None
        
        """ Lower bound.
        Type `float`. """
        
        self._from_fhir = None
        
        """ extension for fhir primitive  from_fhir"""
        
        self.level = None
        
        """ Level of confidence interval.
        Type `float`. """
        
        self._level = None
        
        """ extension for fhir primitive  level"""
        
        self.to = None
        
        """ Upper bound.
        Type `float`. """
        
        self._to = None
        
        """ extension for fhir primitive  to"""
        
        self.type = None
        
        """ Type of precision estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("from_fhir", "from", float, False, None, False),
            ("_from_fhir", "_from",fhirprimitive.FHIRPrimitive, False, None, False),
            ("level", "level", float, False, None, False),
            ("_level", "_level",fhirprimitive.FHIRPrimitive, False, None, False),
            ("to", "to", float, False, None, False),
            ("_to", "_to",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ What sample size was involved?.
    
    A description of the size of the sample involved in the synthesis.
    """
    
    resource_type = "RiskEvidenceSynthesisSampleSize"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Description of sample size.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.numberOfParticipants = None
        
        """ How many participants?.
        Type `int`. """
        
        self._numberOfParticipants = None
        
        """ extension for fhir primitive  numberOfParticipants"""
        
        self.numberOfStudies = None
        
        """ How many studies?.
        Type `int`. """
        
        self._numberOfStudies = None
        
        """ extension for fhir primitive  numberOfStudies"""
        
        super(RiskEvidenceSynthesisSampleSize, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("_numberOfParticipants", "_numberOfParticipants",fhirprimitive.FHIRPrimitive, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
            ("_numberOfStudies", "_numberOfStudies",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import usagecontext
from . import fhirprimitive

