#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Claim) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """
    
    resource_type = "Claim"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None
        
        """ Details about an accident.
        Type `ClaimAccident` (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        
        """ Period for charge submission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.careTeam = None
        
        """ Members of the care team.
        List of `ClaimCareTeam` items (represented as `dict` in JSON). """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        
        """ List of Diagnosis.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.enterer = None
        
        """ Author.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility = None
        
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fundsReserve = None
        
        """ Funds requested to be reserved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.information = None
        
        """ Exceptions, special considerations, the condition, situation, prior
        or concurrent issues.
        List of `ClaimInformation` items (represented as `dict` in JSON). """
        
        self.insurance = None
        
        """ Insurance or medical plan.
        List of `ClaimInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Goods and Services.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.originalPrescription = None
        
        """ Original prescription if superseded by fulfiller.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        
        """ The subject of the Products and Services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee = None
        
        """ Party to be paid any benefits payable.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.prescription = None
        
        """ Prescription authorizing services or products.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedure = None
        
        """ Procedures performed.
        List of `ClaimProcedure` items (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Responsible provider.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referral = None
        
        """ Treatment Referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.related = None
        
        """ Related Claims which may be relevant to processing this claim.
        List of `ClaimRelated` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subType = None
        
        """ Finer grained claim type information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.total = None
        
        """ Total claim cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        
        """ claim | preauthorization | predetermination.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", ClaimAccident, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("information", "information", ClaimInformation, True, None, False),
            ("insurance", "insurance", ClaimInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("related", "related", ClaimRelated, True, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("total", "total", money.Money, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ClaimAccident(backboneelement.BackboneElement):
    """ Details about an accident.
    
    An accident which resulted in the need for healthcare services.
    """
    
    resource_type = "ClaimAccident"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        
        """ When the accident occurred
        see information codes
        see information codes.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.locationAddress = None
        
        """ Accident Place.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference = None
        
        """ Accident Place.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ The nature of the accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.
    
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """
    
    resource_type = "ClaimCareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.provider = None
        
        """ Provider individual or organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.qualification = None
        
        """ Type, classification or Specialization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.responsible = None
        
        """ Billing provider.
        Type `bool`. """
        
        self._responsible = None
        
        """ extension for fhir primitive  responsible"""
        
        self.role = None
        
        """ Role on the team.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Number to convey order of careTeam.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("_responsible", "_responsible",fhirprimitive.FHIRPrimitive, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ List of Diagnosis.
    
    List of patient diagnosis for which care is sought.
    """
    
    resource_type = "ClaimDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        
        """ Patient's diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference = None
        
        """ Patient's diagnosis.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onAdmission = None
        
        """ Present on admission.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.packageCode = None
        
        """ Package billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Number to convey order of diagnosis.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.type = None
        
        """ Timing or nature of the diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ClaimInformation(backboneelement.BackboneElement):
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    multiple jurisdiction specific valuesets which are required.
    """
    
    resource_type = "ClaimInformation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        
        """ General class of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        
        """ Type of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        
        """ Reason associated with the information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Information instance identifier.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.timingDate = None
        
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        
        """ Additional Data or supporting information.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        
        """ Additional Data or supporting information.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueQuantity = None
        
        """ Additional Data or supporting information.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ Additional Data or supporting information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Additional Data or supporting information.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        super(ClaimInformation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimInformation, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimInsurance(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_type = "ClaimInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
        
        """ Business agreement.
        Type `str`. """
        
        self._businessArrangement = None
        
        """ extension for fhir primitive  businessArrangement"""
        
        self.claimResponse = None
        
        """ Adjudication results.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage = None
        
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focal = None
        
        """ Is the focal Coverage.
        Type `bool`. """
        
        self._focal = None
        
        """ extension for fhir primitive  focal"""
        
        self.identifier = None
        
        """ Claim number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self._preAuthRef = None
        
        """ extension for fhir primitive  preAuthRef"""
        
        self.sequence = None
        
        """ Service instance identifier.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("_businessArrangement", "_businessArrangement",fhirprimitive.FHIRPrimitive, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("_focal", "_focal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("_preAuthRef", "_preAuthRef",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    resource_type = "ClaimItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        
        """ Service Location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.careTeamSequence = None
        
        """ Applicable careTeam members.
        List of `int` items. """
        
        self._careTeamSequence = None
        
        """ extension for fhir primitive  careTeamSequence"""
        
        self.category = None
        
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        
        """ Additional items.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisSequence = None
        
        """ Applicable diagnoses.
        List of `int` items. """
        
        self._diagnosisSequence = None
        
        """ extension for fhir primitive  diagnosisSequence"""
        
        self.encounter = None
        
        """ Encounters related to this billed item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.informationSequence = None
        
        """ Applicable exception and supporting information.
        List of `int` items. """
        
        self._informationSequence = None
        
        """ extension for fhir primitive  informationSequence"""
        
        self.locationAddress = None
        
        """ Place of service.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept = None
        
        """ Place of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference = None
        
        """ Place of service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.procedureSequence = None
        
        """ Applicable procedures.
        List of `int` items. """
        
        self._procedureSequence = None
        
        """ extension for fhir primitive  procedureSequence"""
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.servicedDate = None
        
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
        
        """ Service Sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.udi = None
        
        """ Unique Device Identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("_careTeamSequence", "_careTeamSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("_diagnosisSequence", "_diagnosisSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("_informationSequence", "_informationSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("_procedureSequence", "_procedureSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    resource_type = "ClaimItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Total additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.subDetail = None
        
        """ Additional items.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.udi = None
        
        """ Unique Device Identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    resource_type = "ClaimItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.billcode = None
        
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.modifier = None
        
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        
        """ Net additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        self.udi = None
        
        """ Unique Device Identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimPayee(backboneelement.BackboneElement):
    """ Party to be paid any benefits payable.
    
    The party to be reimbursed for the services.
    """
    
    resource_type = "ClaimPayee"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        
        """ Party to receive the payable.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.resource = None
        
        """ organization | patient | practitioner | relatedperson.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type of party: Subscriber, Provider, other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("resource", "resource", coding.Coding, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ClaimProcedure(backboneelement.BackboneElement):
    """ Procedures performed.
    
    Ordered list of patient procedures performed to support the adjudication.
    """
    
    resource_type = "ClaimProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.procedureCodeableConcept = None
        
        """ Patient's list of procedures performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedureReference = None
        
        """ Patient's list of procedures performed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sequence = None
        
        """ Procedure sequence for reference.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimRelated(backboneelement.BackboneElement):
    """ Related Claims which may be relevant to processing this claim.
    
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """
    
    resource_type = "ClaimRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claim = None
        
        """ Reference to the related claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reference = None
        
        """ Related file or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relationship = None
        
        """ How the reference claim is related.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import fhirprimitive

