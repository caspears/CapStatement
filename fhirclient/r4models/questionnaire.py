#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    
    resource_type = "Questionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        
        """ When the questionnaire was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.code = None
        
        """ Concept that represents the overall questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
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
        
        self.derivedFrom = None
        
        """ Instantiates protocol or definition.
        List of `str` items. """
        
        self._derivedFrom = None
        
        """ extension for fhir primitive  derivedFrom"""
        
        self.description = None
        
        """ Natural language description of the questionnaire.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.effectivePeriod = None
        
        """ When the questionnaire is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.identifier = None
        
        """ Additional identifier for the questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Questions and sections within the Questionnaire.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for questionnaire (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        
        """ When the questionnaire was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        
        """ Name for this questionnaire (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this questionnaire is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subjectType = None
        
        """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """
        
        self._subjectType = None
        
        """ extension for fhir primitive  subjectType"""
        
        self.title = None
        
        """ Name for this questionnaire (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Canonical identifier for this questionnaire, represented as a URI
        (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the questionnaire.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", str, True, None, False),
            ("_derivedFrom", "_derivedFrom",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subjectType", "subjectType", str, True, None, False),
            ("_subjectType", "_subjectType",fhirprimitive.FHIRPrimitive, False, None, False),
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

class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    
    resource_type = "QuestionnaireItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answerOption = None
        
        """ Permitted answer.
        List of `QuestionnaireItemAnswerOption` items (represented as `dict` in JSON). """
        
        self.answerValueSet = None
        
        """ Valueset containing permitted answers.
        Type `str`. """
        
        self._answerValueSet = None
        
        """ extension for fhir primitive  answerValueSet"""
        
        self.code = None
        
        """ Corresponding concept for this item in a terminology.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.definition = None
        
        """ ElementDefinition - details for the item.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.enableBehavior = None
        
        """ all | any.
        Type `str`. """
        
        self._enableBehavior = None
        
        """ extension for fhir primitive  enableBehavior"""
        
        self.enableWhen = None
        
        """ Only allow data when.
        List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON). """
        
        self.initial = None
        
        """ Initial value(s) when item is first rendered.
        List of `QuestionnaireItemInitial` items (represented as `dict` in JSON). """
        
        self.item = None
        
        """ Nested questionnaire items.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.linkId = None
        
        """ Unique id for item in questionnaire.
        Type `str`. """
        
        self._linkId = None
        
        """ extension for fhir primitive  linkId"""
        
        self.maxLength = None
        
        """ No more than this many characters.
        Type `int`. """
        
        self._maxLength = None
        
        """ extension for fhir primitive  maxLength"""
        
        self.prefix = None
        
        """ E.g. "1(a)", "2.5.3".
        Type `str`. """
        
        self._prefix = None
        
        """ extension for fhir primitive  prefix"""
        
        self.readOnly = None
        
        """ Don't allow human editing.
        Type `bool`. """
        
        self._readOnly = None
        
        """ extension for fhir primitive  readOnly"""
        
        self.repeats = None
        
        """ Whether the item may repeat.
        Type `bool`. """
        
        self._repeats = None
        
        """ extension for fhir primitive  repeats"""
        
        self.required = None
        
        """ Whether the item must be included in data results.
        Type `bool`. """
        
        self._required = None
        
        """ extension for fhir primitive  required"""
        
        self.text = None
        
        """ Primary text for the item.
        Type `str`. """
        
        self._text = None
        
        """ extension for fhir primitive  text"""
        
        self.type = None
        
        """ group | display | boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(QuestionnaireItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False),
            ("answerValueSet", "answerValueSet", str, False, None, False),
            ("_answerValueSet", "_answerValueSet",fhirprimitive.FHIRPrimitive, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("enableBehavior", "enableBehavior", str, False, None, False),
            ("_enableBehavior", "_enableBehavior",fhirprimitive.FHIRPrimitive, False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("initial", "initial", QuestionnaireItemInitial, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("_linkId", "_linkId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("_maxLength", "_maxLength",fhirprimitive.FHIRPrimitive, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("_prefix", "_prefix",fhirprimitive.FHIRPrimitive, False, None, False),
            ("readOnly", "readOnly", bool, False, None, False),
            ("_readOnly", "_readOnly",fhirprimitive.FHIRPrimitive, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("_repeats", "_repeats",fhirprimitive.FHIRPrimitive, False, None, False),
            ("required", "required", bool, False, None, False),
            ("_required", "_required",fhirprimitive.FHIRPrimitive, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ Permitted answer.
    
    One of the permitted answers for a "choice" or "open-choice" question.
    """
    
    resource_type = "QuestionnaireItemAnswerOption"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.initialSelected = None
        
        """ Whether option is selected by default.
        Type `bool`. """
        
        self._initialSelected = None
        
        """ extension for fhir primitive  initialSelected"""
        
        self.valueCoding = None
        
        """ Answer value.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
        
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        
        """ Answer value.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueReference = None
        
        """ Answer value.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Answer value.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueTime = None
        
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(QuestionnaireItemAnswerOption, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("initialSelected", "initialSelected", bool, False, None, False),
            ("_initialSelected", "_initialSelected",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
        ])
        return js


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.
    
    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    
    resource_type = "QuestionnaireItemEnableWhen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answerBoolean = None
        
        """ Value for question comparison based on operator.
        Type `bool`. """
        
        self._answerBoolean = None
        
        """ extension for fhir primitive  answerBoolean"""
        
        self.answerCoding = None
        
        """ Value for question comparison based on operator.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.answerDate = None
        
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDateTime = None
        
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDecimal = None
        
        """ Value for question comparison based on operator.
        Type `float`. """
        
        self._answerDecimal = None
        
        """ extension for fhir primitive  answerDecimal"""
        
        self.answerInteger = None
        
        """ Value for question comparison based on operator.
        Type `int`. """
        
        self._answerInteger = None
        
        """ extension for fhir primitive  answerInteger"""
        
        self.answerQuantity = None
        
        """ Value for question comparison based on operator.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.answerReference = None
        
        """ Value for question comparison based on operator.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.answerString = None
        
        """ Value for question comparison based on operator.
        Type `str`. """
        
        self._answerString = None
        
        """ extension for fhir primitive  answerString"""
        
        self.answerTime = None
        
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.operator = None
        
        """ exists | = | != | > | < | >= | <=.
        Type `str`. """
        
        self._operator = None
        
        """ extension for fhir primitive  operator"""
        
        self.question = None
        
        """ Question that determines whether item is enabled.
        Type `str`. """
        
        self._question = None
        
        """ extension for fhir primitive  question"""
        
        super(QuestionnaireItemEnableWhen, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerBoolean", "answerBoolean", bool, False, "answer", True),
            ("_answerBoolean", "_answerBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("answerCoding", "answerCoding", coding.Coding, False, "answer", True),
            ("answerDate", "answerDate", fhirdate.FHIRDate, False, "answer", True),
            ("answerDateTime", "answerDateTime", fhirdate.FHIRDate, False, "answer", True),
            ("answerDecimal", "answerDecimal", float, False, "answer", True),
            ("_answerDecimal", "_answerDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("answerInteger", "answerInteger", int, False, "answer", True),
            ("_answerInteger", "_answerInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("answerQuantity", "answerQuantity", quantity.Quantity, False, "answer", True),
            ("answerReference", "answerReference", fhirreference.FHIRReference, False, "answer", True),
            ("answerString", "answerString", str, False, "answer", True),
            ("_answerString", "_answerString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("answerTime", "answerTime", fhirdate.FHIRDate, False, "answer", True),
            ("operator", "operator", str, False, None, True),
            ("_operator", "_operator",fhirprimitive.FHIRPrimitive, False, None, False),
            ("question", "question", str, False, None, True),
            ("_question", "_question",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ Initial value(s) when item is first rendered.
    
    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    
    resource_type = "QuestionnaireItemInitial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueAttachment = None
        
        """ Actual value for initializing the question.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        
        """ Actual value for initializing the question.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueCoding = None
        
        """ Actual value for initializing the question.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
        
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        
        """ Actual value for initializing the question.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueInteger = None
        
        """ Actual value for initializing the question.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueQuantity = None
        
        """ Actual value for initializing the question.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        
        """ Actual value for initializing the question.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
        
        """ Actual value for initializing the question.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        self.valueTime = None
        
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueUri = None
        
        """ Actual value for initializing the question.
        Type `str`. """
        
        self._valueUri = None
        
        """ extension for fhir primitive  valueUri"""
        
        super(QuestionnaireItemInitial, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import usagecontext
from . import fhirprimitive

