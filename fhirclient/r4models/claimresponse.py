#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ClaimResponse(domainresource.DomainResource):
    """ ClaimResponse resource.
    
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    
    resource_type = "ClaimResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addItem = None
        
        """ Insurer added line items.
        List of `ClaimResponseAddItem` items (represented as `dict` in JSON). """
        
        self.communicationRequest = None
        
        """ Request for additional information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.created = None
        
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        
        """ Disposition Message.
        Type `str`. """
        
        self._disposition = None
        
        """ extension for fhir primitive  disposition"""
        
        self.error = None
        
        """ Processing errors.
        List of `ClaimResponseError` items (represented as `dict` in JSON). """
        
        self.form = None
        
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Response  number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance = None
        
        """ Insurance or medical plan.
        List of `ClaimResponseInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        
        """ Insurance issuing organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Line items.
        List of `ClaimResponseItem` items (represented as `dict` in JSON). """
        
        self.outcome = None
        
        """ queued | complete | error | partial.
        Type `str`. """
        
        self._outcome = None
        
        """ extension for fhir primitive  outcome"""
        
        self.patient = None
        
        """ The subject of the Products and Services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payeeType = None
        
        """ Party to be paid any benefits payable.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.payment = None
        
        """ Payment Details.
        Type `ClaimResponsePayment` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        
        """ Pre-Authorization/Determination Reference.
        Type `str`. """
        
        self._preAuthRef = None
        
        """ extension for fhir primitive  preAuthRef"""
        
        self.processNote = None
        
        """ Processing notes.
        List of `ClaimResponseProcessNote` items (represented as `dict` in JSON). """
        
        self.request = None
        
        """ Id of resource triggering adjudication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reserved = None
        
        """ Funds reserved status.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subType = None
        
        """ Finer grained claim type information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.total = None
        
        """ Adjudication totals.
        List of `ClaimResponseTotal` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Type or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        
        """ claim | preauthorization | predetermination.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        super(ClaimResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("addItem", "addItem", ClaimResponseAddItem, True, None, False),
            ("communicationRequest", "communicationRequest", fhirreference.FHIRReference, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("error", "error", ClaimResponseError, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ClaimResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ClaimResponseItem, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("payeeType", "payeeType", codeableconcept.CodeableConcept, False, None, False),
            ("payment", "payment", ClaimResponsePayment, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("_preAuthRef", "_preAuthRef",fhirprimitive.FHIRPrimitive, False, None, False),
            ("processNote", "processNote", ClaimResponseProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("reserved", "reserved", coding.Coding, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("total", "total", ClaimResponseTotal, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first-tier service adjudications for payor added services.
    """
    
    resource_type = "ClaimResponseAddItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Added items adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Group, Service or Product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        
        """ Service Location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        
        """ Insurer added line items.
        List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON). """
        
        self.detailSequence = None
        
        """ Detail sequence number.
        List of `int` items. """
        
        self._detailSequence = None
        
        """ extension for fhir primitive  detailSequence"""
        
        self.factor = None
        
        """ Price scaling factor.
        Type `float`. """
        
        self._factor = None
        
        """ extension for fhir primitive  factor"""
        
        self.itemSequence = None
        
        """ Service instances.
        List of `int` items. """
        
        self._itemSequence = None
        
        """ extension for fhir primitive  itemSequence"""
        
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
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.programCode = None
        
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.provider = None
        
        """ Authorized providers.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
        
        """ Service Sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subdetailSequence = None
        
        """ Subdetail sequence number.
        List of `int` items. """
        
        self._subdetailSequence = None
        
        """ extension for fhir primitive  subdetailSequence"""
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimResponseAddItemDetail, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("_detailSequence", "_detailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("itemSequence", "itemSequence", int, True, None, False),
            ("_itemSequence", "_itemSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("subdetailSequence", "subdetailSequence", int, True, None, False),
            ("_subdetailSequence", "_subdetailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The second-tier service adjudications for payor added services.
    """
    
    resource_type = "ClaimResponseAddItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Added items detail adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Group, Service or Product.
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
        
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.subDetail = None
        
        """ Insurer added line items.
        List of `ClaimResponseAddItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("subDetail", "subDetail", ClaimResponseAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The third-tier service adjudications for payor added services.
    """
    
    resource_type = "ClaimResponseAddItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Added items detail adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.billcode = None
        
        """ Group, Service or Product.
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
        
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.quantity = None
        
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("billcode", "billcode", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    resource_type = "ClaimResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailSequence = None
        
        """ Detail sequence number.
        Type `int`. """
        
        self._detailSequence = None
        
        """ extension for fhir primitive  detailSequence"""
        
        self.itemSequence = None
        
        """ Item sequence number.
        Type `int`. """
        
        self._itemSequence = None
        
        """ extension for fhir primitive  itemSequence"""
        
        self.subDetailSequence = None
        
        """ Subdetail sequence number.
        Type `int`. """
        
        self._subDetailSequence = None
        
        """ extension for fhir primitive  subDetailSequence"""
        
        super(ClaimResponseError, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("detailSequence", "detailSequence", int, False, None, False),
            ("_detailSequence", "_detailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("itemSequence", "itemSequence", int, False, None, False),
            ("_itemSequence", "_itemSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, False),
            ("_subDetailSequence", "_subDetailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_type = "ClaimResponseInsurance"
    
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
        
        self.sequence = None
        
        """ Service instance identifier.
        Type `int`. """
        
        self._sequence = None
        
        """ extension for fhir primitive  sequence"""
        
        super(ClaimResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("_businessArrangement", "_businessArrangement",fhirprimitive.FHIRPrimitive, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("_focal", "_focal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimResponseItem(backboneelement.BackboneElement):
    """ Line items.
    
    The first-tier service adjudications for submitted services.
    """
    
    resource_type = "ClaimResponseItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detail = None
        
        """ Detail line items.
        List of `ClaimResponseItemDetail` items (represented as `dict` in JSON). """
        
        self.itemSequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._itemSequence = None
        
        """ extension for fhir primitive  itemSequence"""
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        super(ClaimResponseItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("detail", "detail", ClaimResponseItemDetail, True, None, False),
            ("itemSequence", "itemSequence", int, False, None, True),
            ("_itemSequence", "_itemSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    The adjudication results.
    """
    
    resource_type = "ClaimResponseItemAdjudication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        
        """ Explanation of Adjudication outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        
        """ Non-monetary value.
        Type `float`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(ClaimResponseItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ Detail line items.
    
    The second-tier service adjudications for submitted services.
    """
    
    resource_type = "ClaimResponseItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Detail level adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detailSequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._detailSequence = None
        
        """ extension for fhir primitive  detailSequence"""
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.subDetail = None
        
        """ Subdetail line items.
        List of `ClaimResponseItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        super(ClaimResponseItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("detailSequence", "detailSequence", int, False, None, True),
            ("_detailSequence", "_detailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subDetail", "subDetail", ClaimResponseItemDetailSubDetail, True, None, False),
        ])
        return js


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ Subdetail line items.
    
    The third-tier service adjudications for submitted services.
    """
    
    resource_type = "ClaimResponseItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        
        """ Subdetail level adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.noteNumber = None
        
        """ List of note numbers which apply.
        List of `int` items. """
        
        self._noteNumber = None
        
        """ extension for fhir primitive  noteNumber"""
        
        self.subDetailSequence = None
        
        """ Service instance.
        Type `int`. """
        
        self._subDetailSequence = None
        
        """ extension for fhir primitive  subDetailSequence"""
        
        super(ClaimResponseItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, True),
            ("_subDetailSequence", "_subDetailSequence",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimResponsePayment(backboneelement.BackboneElement):
    """ Payment Details.
    
    Payment details for the claim if the claim has been paid.
    """
    
    resource_type = "ClaimResponsePayment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjustment = None
        
        """ Payment adjustment for non-Claim issues.
        Type `Money` (represented as `dict` in JSON). """
        
        self.adjustmentReason = None
        
        """ Explanation for the non-claim adjustment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.amount = None
        
        """ Payable amount after adjustment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Expected data of Payment.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        
        """ Identifier of the payment instrument.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ Partial or Complete.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponsePayment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponsePayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """ Processing notes.
    
    Note text.
    """
    
    resource_type = "ClaimResponseProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        
        """ Language if different from the resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.number = None
        
        """ Sequence Number for this note.
        Type `int`. """
        
        self._number = None
        
        """ extension for fhir primitive  number"""
        
        self.text = None
        
        """ Note explanatory text.
        Type `str`. """
        
        self._text = None
        
        """ extension for fhir primitive  text"""
        
        self.type = None
        
        """ display | print | printoper.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(ClaimResponseProcessNote, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("_number", "_number",fhirprimitive.FHIRPrimitive, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ClaimResponseTotal(backboneelement.BackboneElement):
    """ Adjudication totals.
    
    Totals for amounts submitted, co-pays, benefits payable etc.
    """
    
    resource_type = "ClaimResponseTotal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        
        """ Adjudication category such as submitted, co-pay, eligible, benefit,
        etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponseTotal, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ClaimResponseTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import address
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import fhirprimitive

