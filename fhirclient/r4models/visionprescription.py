#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.
    
    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """
    
    resource_type = "VisionPrescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        
        """ Response creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dateWritten = None
        
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        
        """ Created during encounter / admission / stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business Identifier for vision prescription.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lensSpecification = None
        
        """ Vision lens authorization.
        List of `VisionPrescriptionLensSpecification` items (represented as `dict` in JSON). """
        
        self.patient = None
        
        """ Who prescription is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prescriber = None
        
        """ Who authorized the vision prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lensSpecification", "lensSpecification", VisionPrescriptionLensSpecification, True, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """ Vision lens authorization.
    
    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """
    
    resource_type = "VisionPrescriptionLensSpecification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.add = None
        
        """ Added power for multifocal levels.
        Type `float`. """
        
        self._add = None
        
        """ extension for fhir primitive  add"""
        
        self.axis = None
        
        """ Lens meridian which contain no power for astigmatism.
        Type `int`. """
        
        self._axis = None
        
        """ extension for fhir primitive  axis"""
        
        self.backCurve = None
        
        """ Contact lens back curvature.
        Type `float`. """
        
        self._backCurve = None
        
        """ extension for fhir primitive  backCurve"""
        
        self.brand = None
        
        """ Brand required.
        Type `str`. """
        
        self._brand = None
        
        """ extension for fhir primitive  brand"""
        
        self.color = None
        
        """ Color required.
        Type `str`. """
        
        self._color = None
        
        """ extension for fhir primitive  color"""
        
        self.cylinder = None
        
        """ Lens power for astigmatism.
        Type `float`. """
        
        self._cylinder = None
        
        """ extension for fhir primitive  cylinder"""
        
        self.diameter = None
        
        """ Contact lens diameter.
        Type `float`. """
        
        self._diameter = None
        
        """ extension for fhir primitive  diameter"""
        
        self.duration = None
        
        """ Lens wear duration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.eye = None
        
        """ right | left.
        Type `str`. """
        
        self._eye = None
        
        """ extension for fhir primitive  eye"""
        
        self.note = None
        
        """ Notes for coatings.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.power = None
        
        """ Contact lens power.
        Type `float`. """
        
        self._power = None
        
        """ extension for fhir primitive  power"""
        
        self.prism = None
        
        """ Eye alignment compensation.
        List of `VisionPrescriptionLensSpecificationPrism` items (represented as `dict` in JSON). """
        
        self.product = None
        
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sphere = None
        
        """ Power of the lens.
        Type `float`. """
        
        self._sphere = None
        
        """ extension for fhir primitive  sphere"""
        
        super(VisionPrescriptionLensSpecification, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecification, self).elementProperties()
        js.extend([
            ("add", "add", float, False, None, False),
            ("_add", "_add",fhirprimitive.FHIRPrimitive, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("_axis", "_axis",fhirprimitive.FHIRPrimitive, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("_backCurve", "_backCurve",fhirprimitive.FHIRPrimitive, False, None, False),
            ("brand", "brand", str, False, None, False),
            ("_brand", "_brand",fhirprimitive.FHIRPrimitive, False, None, False),
            ("color", "color", str, False, None, False),
            ("_color", "_color",fhirprimitive.FHIRPrimitive, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("_cylinder", "_cylinder",fhirprimitive.FHIRPrimitive, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("_diameter", "_diameter",fhirprimitive.FHIRPrimitive, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("eye", "eye", str, False, None, True),
            ("_eye", "_eye",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("power", "power", float, False, None, False),
            ("_power", "_power",fhirprimitive.FHIRPrimitive, False, None, False),
            ("prism", "prism", VisionPrescriptionLensSpecificationPrism, True, None, False),
            ("product", "product", codeableconcept.CodeableConcept, False, None, True),
            ("sphere", "sphere", float, False, None, False),
            ("_sphere", "_sphere",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """ Eye alignment compensation.
    
    Allows for adjustment on two axis.
    """
    
    resource_type = "VisionPrescriptionLensSpecificationPrism"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        
        """ Amount of adjustment.
        Type `float`. """
        
        self._amount = None
        
        """ extension for fhir primitive  amount"""
        
        self.base = None
        
        """ up | down | in | out.
        Type `str`. """
        
        self._base = None
        
        """ extension for fhir primitive  base"""
        
        super(VisionPrescriptionLensSpecificationPrism, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecificationPrism, self).elementProperties()
        js.extend([
            ("amount", "amount", float, False, None, True),
            ("_amount", "_amount",fhirprimitive.FHIRPrimitive, False, None, False),
            ("base", "base", str, False, None, True),
            ("_base", "_base",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import fhirprimitive

