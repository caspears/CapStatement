#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/ExampleScenario) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class ExampleScenario(domainresource.DomainResource):
    """ Example of workflow instance.
    """
    
    resource_type = "ExampleScenario"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        
        """ Actor participating in the resource.
        List of `ExampleScenarioActor` items (represented as `dict` in JSON). """
        
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
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.identifier = None
        
        """ Additional identifier for the example scenario.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instance = None
        
        """ Each resource and each version that is present in the workflow.
        List of `ExampleScenarioInstance` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for example scenario (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this example scenario (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.process = None
        
        """ Each major process - a group of operations.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ The purpose of the example, e.g. to illustrate a scenario.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.url = None
        
        """ Canonical identifier for this example scenario, represented as a
        URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the example scenario.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        self.workflow = None
        
        """ Another nested workflow.
        List of `str` items. """
        
        self._workflow = None
        
        """ extension for fhir primitive  workflow"""
        
        super(ExampleScenario, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenario, self).elementProperties()
        js.extend([
            ("actor", "actor", ExampleScenarioActor, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instance", "instance", ExampleScenarioInstance, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
            ("workflow", "workflow", str, True, None, False),
            ("_workflow", "_workflow",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class ExampleScenarioActor(backboneelement.BackboneElement):
    """ Actor participating in the resource.
    """
    
    resource_type = "ExampleScenarioActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actorId = None
        
        """ ID or acronym of the actor.
        Type `str`. """
        
        self._actorId = None
        
        """ extension for fhir primitive  actorId"""
        
        self.description = None
        
        """ The description of the actor.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.name = None
        
        """ The name of the actor as shown in the page.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.type = None
        
        """ person | entity.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(ExampleScenarioActor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioActor, self).elementProperties()
        js.extend([
            ("actorId", "actorId", str, False, None, True),
            ("_actorId", "_actorId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExampleScenarioInstance(backboneelement.BackboneElement):
    """ Each resource and each version that is present in the workflow.
    """
    
    resource_type = "ExampleScenarioInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.containedInstance = None
        
        """ Resources contained in the instance.
        List of `ExampleScenarioInstanceContainedInstance` items (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Human-friendly description of the resource instance.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.name = None
        
        """ A short name for the resource instance.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.resourceId = None
        
        """ The id of the resource for referencing.
        Type `str`. """
        
        self._resourceId = None
        
        """ extension for fhir primitive  resourceId"""
        
        self.resourceType = None
        
        """ The type of the resource.
        Type `str`. """
        
        self._resourceType = None
        
        """ extension for fhir primitive  resourceType"""
        
        self.version = None
        
        """ A specific version of the resource.
        List of `ExampleScenarioInstanceVersion` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioInstance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioInstance, self).elementProperties()
        js.extend([
            ("containedInstance", "containedInstance", ExampleScenarioInstanceContainedInstance, True, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("resourceId", "resourceId", str, False, None, True),
            ("_resourceId", "_resourceId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("resourceType", "resourceType", str, False, None, True),
            ("_resourceType", "_resourceType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", ExampleScenarioInstanceVersion, True, None, False),
        ])
        return js


class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """ Resources contained in the instance.
    
    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """
    
    resource_type = "ExampleScenarioInstanceContainedInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resourceId = None
        
        """ Each resource contained in the instance.
        Type `str`. """
        
        self._resourceId = None
        
        """ extension for fhir primitive  resourceId"""
        
        self.versionId = None
        
        """ A specific version of a resource contained in the instance.
        Type `str`. """
        
        self._versionId = None
        
        """ extension for fhir primitive  versionId"""
        
        super(ExampleScenarioInstanceContainedInstance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioInstanceContainedInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", str, False, None, True),
            ("_resourceId", "_resourceId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("versionId", "versionId", str, False, None, False),
            ("_versionId", "_versionId",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """ A specific version of the resource.
    """
    
    resource_type = "ExampleScenarioInstanceVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ The description of the resource version.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.versionId = None
        
        """ The identifier of a specific version of a resource.
        Type `str`. """
        
        self._versionId = None
        
        """ extension for fhir primitive  versionId"""
        
        super(ExampleScenarioInstanceVersion, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioInstanceVersion, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("versionId", "versionId", str, False, None, True),
            ("_versionId", "_versionId",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExampleScenarioProcess(backboneelement.BackboneElement):
    """ Each major process - a group of operations.
    """
    
    resource_type = "ExampleScenarioProcess"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ A longer description of the group of operations.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.postConditions = None
        
        """ Description of final status after the process ends.
        Type `str`. """
        
        self._postConditions = None
        
        """ extension for fhir primitive  postConditions"""
        
        self.preConditions = None
        
        """ Description of initial status before the process starts.
        Type `str`. """
        
        self._preConditions = None
        
        """ extension for fhir primitive  preConditions"""
        
        self.step = None
        
        """ Each step of the process.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        self.title = None
        
        """ The diagram title of the group of operations.
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        super(ExampleScenarioProcess, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcess, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("postConditions", "postConditions", str, False, None, False),
            ("_postConditions", "_postConditions",fhirprimitive.FHIRPrimitive, False, None, False),
            ("preConditions", "preConditions", str, False, None, False),
            ("_preConditions", "_preConditions",fhirprimitive.FHIRPrimitive, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """ Each step of the process.
    """
    
    resource_type = "ExampleScenarioProcessStep"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alternative = None
        
        """ Alternate non-typical step action.
        List of `ExampleScenarioProcessStepAlternative` items (represented as `dict` in JSON). """
        
        self.operation = None
        
        """ Each interaction or action.
        Type `ExampleScenarioProcessStepOperation` (represented as `dict` in JSON). """
        
        self.pause = None
        
        """ If there is a pause in the flow.
        Type `bool`. """
        
        self._pause = None
        
        """ extension for fhir primitive  pause"""
        
        self.process = None
        
        """ Nested process.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioProcessStep, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcessStep, self).elementProperties()
        js.extend([
            ("alternative", "alternative", ExampleScenarioProcessStepAlternative, True, None, False),
            ("operation", "operation", ExampleScenarioProcessStepOperation, False, None, False),
            ("pause", "pause", bool, False, None, False),
            ("_pause", "_pause",fhirprimitive.FHIRPrimitive, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
        ])
        return js


class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """ Alternate non-typical step action.
    
    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """
    
    resource_type = "ExampleScenarioProcessStepAlternative"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ A human-readable description of each option.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.step = None
        
        """ What happens in each alternative option.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        self.title = None
        
        """ Label for alternative.
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        super(ExampleScenarioProcessStepAlternative, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcessStepAlternative, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """ Each interaction or action.
    """
    
    resource_type = "ExampleScenarioProcessStepOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        
        """ A comment to be inserted in the diagram.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.initiator = None
        
        """ Who starts the transaction.
        Type `str`. """
        
        self._initiator = None
        
        """ extension for fhir primitive  initiator"""
        
        self.initiatorActive = None
        
        """ Whether the initiator is deactivated right after the transaction.
        Type `bool`. """
        
        self._initiatorActive = None
        
        """ extension for fhir primitive  initiatorActive"""
        
        self.name = None
        
        """ The human-friendly name of the interaction.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.number = None
        
        """ The sequential number of the interaction.
        Type `str`. """
        
        self._number = None
        
        """ extension for fhir primitive  number"""
        
        self.receiver = None
        
        """ Who receives the transaction.
        Type `str`. """
        
        self._receiver = None
        
        """ extension for fhir primitive  receiver"""
        
        self.receiverActive = None
        
        """ Whether the receiver is deactivated right after the transaction.
        Type `bool`. """
        
        self._receiverActive = None
        
        """ extension for fhir primitive  receiverActive"""
        
        self.request = None
        
        """ Each resource instance used by the initiator.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        self.response = None
        
        """ Each resource instance used by the responder.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ The type of operation - CRUD.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(ExampleScenarioProcessStepOperation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExampleScenarioProcessStepOperation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("initiator", "initiator", str, False, None, False),
            ("_initiator", "_initiator",fhirprimitive.FHIRPrimitive, False, None, False),
            ("initiatorActive", "initiatorActive", bool, False, None, False),
            ("_initiatorActive", "_initiatorActive",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("number", "number", str, False, None, True),
            ("_number", "_number",fhirprimitive.FHIRPrimitive, False, None, False),
            ("receiver", "receiver", str, False, None, False),
            ("_receiver", "_receiver",fhirprimitive.FHIRPrimitive, False, None, False),
            ("receiverActive", "receiverActive", bool, False, None, False),
            ("_receiverActive", "_receiverActive",fhirprimitive.FHIRPrimitive, False, None, False),
            ("request", "request", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("response", "response", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import identifier
from . import usagecontext
from . import fhirprimitive

