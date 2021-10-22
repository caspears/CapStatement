#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class RequestGroup(domainresource.DomainResource):
    """ A group of related requests.
    
    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    
    resource_type = "RequestGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        
        """ Proposed actions, if any.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        self.author = None
        
        """ Device or practitioner that authored the request group.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        
        """ When the request group was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        
        """ Fulfills plan, proposal, or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code = None
        
        """ What's being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
        
        """ Encounter or Episode for the request group.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self._instantiatesCanonical = None
        
        """ extension for fhir primitive  instantiatesCanonical"""
        
        self.instantiatesUri = None
        
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self._instantiatesUri = None
        
        """ extension for fhir primitive  instantiatesUri"""
        
        self.intent = None
        
        """ proposal | plan | order.
        Type `str`. """
        
        self._intent = None
        
        """ extension for fhir primitive  intent"""
        
        self.note = None
        
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.priority = None
        
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        self.reasonCode = None
        
        """ Why the request group is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        
        """ Why the request group is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        
        """ Request(s) replaced by this request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | suspended | cancelled | completed | entered-in-
        error | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.subject = None
        
        """ Who the request group is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(RequestGroup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class RequestGroupAction(backboneelement.BackboneElement):
    """ Proposed actions, if any.
    
    The actions, if any, produced by the evaluation of the artifact.
    """
    
    resource_type = "RequestGroupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        
        """ Sub action.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        self.cardinalityBehavior = None
        
        """ single | multiple.
        Type `str`. """
        
        self._cardinalityBehavior = None
        
        """ extension for fhir primitive  cardinalityBehavior"""
        
        self.code = None
        
        """ Code representing the meaning of the action or sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.condition = None
        
        """ Whether or not the action is applicable.
        List of `RequestGroupActionCondition` items (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Short description of the action.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.documentation = None
        
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.groupingBehavior = None
        
        """ visual-group | logical-group | sentence-group.
        Type `str`. """
        
        self._groupingBehavior = None
        
        """ extension for fhir primitive  groupingBehavior"""
        
        self.participant = None
        
        """ Who should perform the action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.precheckBehavior = None
        
        """ yes | no.
        Type `str`. """
        
        self._precheckBehavior = None
        
        """ extension for fhir primitive  precheckBehavior"""
        
        self.prefix = None
        
        """ User-visible prefix for the action (e.g. 1. or A.).
        Type `str`. """
        
        self._prefix = None
        
        """ extension for fhir primitive  prefix"""
        
        self.priority = None
        
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self._priority = None
        
        """ extension for fhir primitive  priority"""
        
        self.relatedAction = None
        
        """ Relationship to another action.
        List of `RequestGroupActionRelatedAction` items (represented as `dict` in JSON). """
        
        self.requiredBehavior = None
        
        """ must | could | must-unless-documented.
        Type `str`. """
        
        self._requiredBehavior = None
        
        """ extension for fhir primitive  requiredBehavior"""
        
        self.resource = None
        
        """ The target of the action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.selectionBehavior = None
        
        """ any | all | all-or-none | exactly-one | at-most-one | one-or-more.
        Type `str`. """
        
        self._selectionBehavior = None
        
        """ extension for fhir primitive  selectionBehavior"""
        
        self.textEquivalent = None
        
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `str`. """
        
        self._textEquivalent = None
        
        """ extension for fhir primitive  textEquivalent"""
        
        self.timingAge = None
        
        """ When the action should take place.
        Type `Age` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        
        """ When the action should take place.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDuration = None
        
        """ When the action should take place.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        
        """ When the action should take place.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingRange = None
        
        """ When the action should take place.
        Type `Range` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        
        """ When the action should take place.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        
        """ User-visible title.
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.type = None
        
        """ create | update | remove | fire-event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(RequestGroupAction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("_cardinalityBehavior", "_cardinalityBehavior",fhirprimitive.FHIRPrimitive, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("_groupingBehavior", "_groupingBehavior",fhirprimitive.FHIRPrimitive, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("_precheckBehavior", "_precheckBehavior",fhirprimitive.FHIRPrimitive, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("_prefix", "_prefix",fhirprimitive.FHIRPrimitive, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority",fhirprimitive.FHIRPrimitive, False, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("_requiredBehavior", "_requiredBehavior",fhirprimitive.FHIRPrimitive, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("_selectionBehavior", "_selectionBehavior",fhirprimitive.FHIRPrimitive, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("_textEquivalent", "_textEquivalent",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class RequestGroupActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """
    
    resource_type = "RequestGroupActionCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ Natural language description of the condition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.expression = None
        
        """ Boolean-valued expression.
        Type `str`. """
        
        self._expression = None
        
        """ extension for fhir primitive  expression"""
        
        self.kind = None
        
        """ applicability | start | stop.
        Type `str`. """
        
        self._kind = None
        
        """ extension for fhir primitive  kind"""
        
        self.language = None
        
        """ Language of the expression.
        Type `str`. """
        
        self._language = None
        
        """ extension for fhir primitive  language"""
        
        super(RequestGroupActionCondition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression",fhirprimitive.FHIRPrimitive, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind",fhirprimitive.FHIRPrimitive, False, None, False),
            ("language", "language", str, False, None, False),
            ("_language", "_language",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    resource_type = "RequestGroupActionRelatedAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionId = None
        
        """ What action this is related to.
        Type `str`. """
        
        self._actionId = None
        
        """ extension for fhir primitive  actionId"""
        
        self.offsetDuration = None
        
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.offsetRange = None
        
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """
        
        self.relationship = None
        
        """ before-start | before | before-end | concurrent-with-start |
        concurrent | concurrent-with-end | after-start | after | after-end.
        Type `str`. """
        
        self._relationship = None
        
        """ extension for fhir primitive  relationship"""
        
        super(RequestGroupActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("_actionId", "_actionId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
            ("_relationship", "_relationship",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import age
from . import annotation
from . import codeableconcept
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import relatedartifact
from . import timing
from . import fhirprimitive

