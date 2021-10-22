#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/MolecularSequence) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class MolecularSequence(domainresource.DomainResource):
    """ Information about a biological sequence.
    
    Raw data describing a biological sequence.
    """
    
    resource_type = "MolecularSequence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coordinateSystem = None
        
        """ Base number of coordinate system (0 for 0-based numbering or
        coordinates, inclusive start, exclusive end, 1 for 1-based
        numbering, inclusive start, inclusive end).
        Type `int`. """
        
        self._coordinateSystem = None
        
        """ extension for fhir primitive  coordinateSystem"""
        
        self.device = None
        
        """ The method for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Unique ID for this particular sequence. This is a FHIR-defined id.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.observedSeq = None
        
        """ Sequence that was observed.
        Type `str`. """
        
        self._observedSeq = None
        
        """ extension for fhir primitive  observedSeq"""
        
        self.patient = None
        
        """ Who and/or what this is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        
        """ Who should be responsible for test result.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.pointer = None
        
        """ Pointer to next atomic sequence.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quality = None
        
        """ An set of value as quality of sequence.
        List of `MolecularSequenceQuality` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ The number of copies of the sequence of interest.  (RNASeq).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.readCoverage = None
        
        """ Average number of reads representing a given nucleotide in the
        reconstructed sequence.
        Type `int`. """
        
        self._readCoverage = None
        
        """ extension for fhir primitive  readCoverage"""
        
        self.referenceSeq = None
        
        """ A sequence used as reference.
        Type `MolecularSequenceReferenceSeq` (represented as `dict` in JSON). """
        
        self.repository = None
        
        """ External repository which contains detailed report related with
        observedSeq in this resource.
        List of `MolecularSequenceRepository` items (represented as `dict` in JSON). """
        
        self.specimen = None
        
        """ Specimen used for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.structureVariant = None
        
        """ Structural variant.
        List of `MolecularSequenceStructureVariant` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ aa | dna | rna.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.variant = None
        
        """ Variant in sequence.
        List of `MolecularSequenceVariant` items (represented as `dict` in JSON). """
        
        super(MolecularSequence, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("_coordinateSystem", "_coordinateSystem",fhirprimitive.FHIRPrimitive, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("_observedSeq", "_observedSeq",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("_readCoverage", "_readCoverage",fhirprimitive.FHIRPrimitive, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
        ])
        return js


from . import backboneelement

class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.
    
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    
    resource_type = "MolecularSequenceQuality"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        
        """ End position of the sequence.
        Type `int`. """
        
        self._end = None
        
        """ extension for fhir primitive  end"""
        
        self.fScore = None
        
        """ F-score.
        Type `float`. """
        
        self._fScore = None
        
        """ extension for fhir primitive  fScore"""
        
        self.gtFP = None
        
        """ False positives where the non-REF alleles in the Truth and Query
        Call Sets match.
        Type `float`. """
        
        self._gtFP = None
        
        """ extension for fhir primitive  gtFP"""
        
        self.method = None
        
        """ Method to get quality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.precision = None
        
        """ Precision of comparison.
        Type `float`. """
        
        self._precision = None
        
        """ extension for fhir primitive  precision"""
        
        self.queryFP = None
        
        """ False positives.
        Type `float`. """
        
        self._queryFP = None
        
        """ extension for fhir primitive  queryFP"""
        
        self.queryTP = None
        
        """ True positives from the perspective of the query data.
        Type `float`. """
        
        self._queryTP = None
        
        """ extension for fhir primitive  queryTP"""
        
        self.recall = None
        
        """ Recall of comparison.
        Type `float`. """
        
        self._recall = None
        
        """ extension for fhir primitive  recall"""
        
        self.roc = None
        
        """ Receiver Operator Characteristic (ROC) Curve.
        Type `MolecularSequenceQualityRoc` (represented as `dict` in JSON). """
        
        self.score = None
        
        """ Quality score for the comparison.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.standardSequence = None
        
        """ Standard sequence for comparison.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start = None
        
        """ Start position of the sequence.
        Type `int`. """
        
        self._start = None
        
        """ extension for fhir primitive  start"""
        
        self.truthFN = None
        
        """ False negatives.
        Type `float`. """
        
        self._truthFN = None
        
        """ extension for fhir primitive  truthFN"""
        
        self.truthTP = None
        
        """ True positives from the perspective of the truth data.
        Type `float`. """
        
        self._truthTP = None
        
        """ extension for fhir primitive  truthTP"""
        
        self.type = None
        
        """ indel | snp | unknown.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(MolecularSequenceQuality, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("_end", "_end",fhirprimitive.FHIRPrimitive, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("_fScore", "_fScore",fhirprimitive.FHIRPrimitive, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("_gtFP", "_gtFP",fhirprimitive.FHIRPrimitive, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("_precision", "_precision",fhirprimitive.FHIRPrimitive, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("_queryFP", "_queryFP",fhirprimitive.FHIRPrimitive, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("_queryTP", "_queryTP",fhirprimitive.FHIRPrimitive, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("_recall", "_recall",fhirprimitive.FHIRPrimitive, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start",fhirprimitive.FHIRPrimitive, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("_truthFN", "_truthFN",fhirprimitive.FHIRPrimitive, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("_truthTP", "_truthTP",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.
    
    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """
    
    resource_type = "MolecularSequenceQualityRoc"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fMeasure = None
        
        """ FScore of the GQ score.
        List of `float` items. """
        
        self._fMeasure = None
        
        """ extension for fhir primitive  fMeasure"""
        
        self.numFN = None
        
        """ Roc score false negative numbers.
        List of `int` items. """
        
        self._numFN = None
        
        """ extension for fhir primitive  numFN"""
        
        self.numFP = None
        
        """ Roc score false positive numbers.
        List of `int` items. """
        
        self._numFP = None
        
        """ extension for fhir primitive  numFP"""
        
        self.numTP = None
        
        """ Roc score true positive numbers.
        List of `int` items. """
        
        self._numTP = None
        
        """ extension for fhir primitive  numTP"""
        
        self.precision = None
        
        """ Precision of the GQ score.
        List of `float` items. """
        
        self._precision = None
        
        """ extension for fhir primitive  precision"""
        
        self.score = None
        
        """ Genotype quality score.
        List of `int` items. """
        
        self._score = None
        
        """ extension for fhir primitive  score"""
        
        self.sensitivity = None
        
        """ Sensitivity of the GQ score.
        List of `float` items. """
        
        self._sensitivity = None
        
        """ extension for fhir primitive  sensitivity"""
        
        super(MolecularSequenceQualityRoc, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend([
            ("fMeasure", "fMeasure", float, True, None, False),
            ("_fMeasure", "_fMeasure",fhirprimitive.FHIRPrimitive, False, None, False),
            ("numFN", "numFN", int, True, None, False),
            ("_numFN", "_numFN",fhirprimitive.FHIRPrimitive, False, None, False),
            ("numFP", "numFP", int, True, None, False),
            ("_numFP", "_numFP",fhirprimitive.FHIRPrimitive, False, None, False),
            ("numTP", "numTP", int, True, None, False),
            ("_numTP", "_numTP",fhirprimitive.FHIRPrimitive, False, None, False),
            ("precision", "precision", float, True, None, False),
            ("_precision", "_precision",fhirprimitive.FHIRPrimitive, False, None, False),
            ("score", "score", int, True, None, False),
            ("_score", "_score",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sensitivity", "sensitivity", float, True, None, False),
            ("_sensitivity", "_sensitivity",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.
    
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    
    resource_type = "MolecularSequenceReferenceSeq"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chromosome = None
        
        """ Chromosome containing genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genomeBuild = None
        
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `str`. """
        
        self._genomeBuild = None
        
        """ extension for fhir primitive  genomeBuild"""
        
        self.orientation = None
        
        """ sense | antisense.
        Type `str`. """
        
        self._orientation = None
        
        """ extension for fhir primitive  orientation"""
        
        self.referenceSeqId = None
        
        """ Reference identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceSeqPointer = None
        
        """ A pointer to another MolecularSequence entity as reference sequence.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceSeqString = None
        
        """ A string to represent reference sequence.
        Type `str`. """
        
        self._referenceSeqString = None
        
        """ extension for fhir primitive  referenceSeqString"""
        
        self.strand = None
        
        """ watson | crick.
        Type `str`. """
        
        self._strand = None
        
        """ extension for fhir primitive  strand"""
        
        self.windowEnd = None
        
        """ End position of the window on the reference sequence.
        Type `int`. """
        
        self._windowEnd = None
        
        """ extension for fhir primitive  windowEnd"""
        
        self.windowStart = None
        
        """ Start position of the window on the  reference sequence.
        Type `int`. """
        
        self._windowStart = None
        
        """ extension for fhir primitive  windowStart"""
        
        super(MolecularSequenceReferenceSeq, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("_genomeBuild", "_genomeBuild",fhirprimitive.FHIRPrimitive, False, None, False),
            ("orientation", "orientation", str, False, None, False),
            ("_orientation", "_orientation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("_referenceSeqString", "_referenceSeqString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("strand", "strand", str, False, None, False),
            ("_strand", "_strand",fhirprimitive.FHIRPrimitive, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
            ("_windowEnd", "_windowEnd",fhirprimitive.FHIRPrimitive, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
            ("_windowStart", "_windowStart",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MolecularSequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.
    
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    
    resource_type = "MolecularSequenceRepository"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.datasetId = None
        
        """ Id of the dataset that used to call for dataset in repository.
        Type `str`. """
        
        self._datasetId = None
        
        """ extension for fhir primitive  datasetId"""
        
        self.name = None
        
        """ Repository's name.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.readsetId = None
        
        """ Id of the read.
        Type `str`. """
        
        self._readsetId = None
        
        """ extension for fhir primitive  readsetId"""
        
        self.type = None
        
        """ directlink | openapi | login | oauth | other.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.url = None
        
        """ URI of the repository.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.variantsetId = None
        
        """ Id of the variantset that used to call for variantset in repository.
        Type `str`. """
        
        self._variantsetId = None
        
        """ extension for fhir primitive  variantsetId"""
        
        super(MolecularSequenceRepository, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend([
            ("datasetId", "datasetId", str, False, None, False),
            ("_datasetId", "_datasetId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("readsetId", "readsetId", str, False, None, False),
            ("_readsetId", "_readsetId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("variantsetId", "variantsetId", str, False, None, False),
            ("_variantsetId", "_variantsetId",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """ Structural variant.
    
    Information about chromosome structure variation.
    """
    
    resource_type = "MolecularSequenceStructureVariant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exact = None
        
        """ Does the structural variant have base pair resolution breakpoints?.
        Type `bool`. """
        
        self._exact = None
        
        """ extension for fhir primitive  exact"""
        
        self.inner = None
        
        """ Structural variant inner.
        Type `MolecularSequenceStructureVariantInner` (represented as `dict` in JSON). """
        
        self.length = None
        
        """ Structural Variant Length.
        Type `int`. """
        
        self._length = None
        
        """ extension for fhir primitive  length"""
        
        self.outer = None
        
        """ Structural variant outer.
        Type `MolecularSequenceStructureVariantOuter` (represented as `dict` in JSON). """
        
        self.variantType = None
        
        """ Structural variant change type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MolecularSequenceStructureVariant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("exact", "exact", bool, False, None, False),
            ("_exact", "_exact",fhirprimitive.FHIRPrimitive, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
            ("length", "length", int, False, None, False),
            ("_length", "_length",fhirprimitive.FHIRPrimitive, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("variantType", "variantType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """ Structural variant inner.
    """
    
    resource_type = "MolecularSequenceStructureVariantInner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        
        """ Structural Variant Inner End.
        Type `int`. """
        
        self._end = None
        
        """ extension for fhir primitive  end"""
        
        self.start = None
        
        """ Structural Variant Inner Start.
        Type `int`. """
        
        self._start = None
        
        """ extension for fhir primitive  start"""
        
        super(MolecularSequenceStructureVariantInner, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("_end", "_end",fhirprimitive.FHIRPrimitive, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """ Structural variant outer.
    """
    
    resource_type = "MolecularSequenceStructureVariantOuter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        
        """ Structural Variant Outer End.
        Type `int`. """
        
        self._end = None
        
        """ extension for fhir primitive  end"""
        
        self.start = None
        
        """ Structural Variant Outer Start.
        Type `int`. """
        
        self._start = None
        
        """ extension for fhir primitive  start"""
        
        super(MolecularSequenceStructureVariantOuter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("_end", "_end",fhirprimitive.FHIRPrimitive, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class MolecularSequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.
    
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    
    resource_type = "MolecularSequenceVariant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cigar = None
        
        """ Extended CIGAR string for aligning the sequence with reference
        bases.
        Type `str`. """
        
        self._cigar = None
        
        """ extension for fhir primitive  cigar"""
        
        self.end = None
        
        """ End position of the variant on the reference sequence.
        Type `int`. """
        
        self._end = None
        
        """ extension for fhir primitive  end"""
        
        self.observedAllele = None
        
        """ Allele that was observed.
        Type `str`. """
        
        self._observedAllele = None
        
        """ extension for fhir primitive  observedAllele"""
        
        self.referenceAllele = None
        
        """ Allele in the reference sequence.
        Type `str`. """
        
        self._referenceAllele = None
        
        """ extension for fhir primitive  referenceAllele"""
        
        self.start = None
        
        """ Start position of the variant on the  reference sequence.
        Type `int`. """
        
        self._start = None
        
        """ extension for fhir primitive  start"""
        
        self.variantPointer = None
        
        """ Pointer to observed variant information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MolecularSequenceVariant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("_cigar", "_cigar",fhirprimitive.FHIRPrimitive, False, None, False),
            ("end", "end", int, False, None, False),
            ("_end", "_end",fhirprimitive.FHIRPrimitive, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("_observedAllele", "_observedAllele",fhirprimitive.FHIRPrimitive, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("_referenceAllele", "_referenceAllele",fhirprimitive.FHIRPrimitive, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start",fhirprimitive.FHIRPrimitive, False, None, False),
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import quantity
from . import fhirprimitive

