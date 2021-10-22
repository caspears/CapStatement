#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource
from . import extensionelement

class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
    
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    
    resource_type = "OperationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.affectsState = None
        
        """ Whether content is changed by the operation.
        Type `bool`. """
        
        self._affectsState = None
        
        """ extension for fhir primitive  affectsState"""
        
        self.base = None
        
        """ Marks this as a profile of the base.
        Type `str`. """
        
        self._base = None
        
        """ extension for fhir primitive  base"""
        
        self.code = None
        
        """ Name used to invoke the operation.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.comment = None
        
        """ Additional information about use.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the operation definition.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.inputProfile = None
        
        """ Validation information for in parameters.
        Type `str`. """
        
        self._inputProfile = None
        
        """ extension for fhir primitive  inputProfile"""
        
        self.instance = None
        
        """ Invoke on an instance?.
        Type `bool`. """
        
        self._instance = None
        
        """ extension for fhir primitive  instance"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for operation definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        
        """ operation | query.
        Type `str`. """
        
        self._kind = None
        
        """ extension for fhir primitive  kind"""
        
        self.name = None
        
        """ Name for this operation definition (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.outputProfile = None
        
        """ Validation information for out parameters.
        Type `str`. """
        
        self._outputProfile = None
        
        """ extension for fhir primitive  outputProfile"""
        
        self.overload = None
        
        """ Define overloaded variants for when  generating code.
        List of `OperationDefinitionOverload` items (represented as `dict` in JSON). """
        
        self.parameter = None
        
        """ Parameters for the operation/query.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this operation definition is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.resource = None
        
        """ Types this operation applies to.
        List of `str` items. """
        
        self._resource = None
        
        """ extension for fhir primitive  resource"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.system = None
        
        """ Invoke at the system level?.
        Type `bool`. """
        
        self._system = None
        
        """ extension for fhir primitive  system"""
        
        self.title = None
        
        """ Name for this operation definition (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.type = None
        
        """ Invoke at the type level?.
        Type `bool`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.url = None
        
        """ Canonical identifier for this operation definition, represented as
        a URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the operation definition.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(OperationDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("affectsState", "affectsState", bool, False, None, False),
            ("_affectsState", "_affectsState",extensionelement.ExtensionElement, True, None, False),
            ("base", "base", str, False, None, False),
            ("_base", "_base",extensionelement.ExtensionElement, True, None, False),
            ("code", "code", str, False, None, True),
            ("_code", "_code",extensionelement.ExtensionElement, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",extensionelement.ExtensionElement, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",extensionelement.ExtensionElement, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",extensionelement.ExtensionElement, True, None, False),
            ("inputProfile", "inputProfile", str, False, None, False),
            ("_inputProfile", "_inputProfile",extensionelement.ExtensionElement, True, None, False),
            ("instance", "instance", bool, False, None, True),
            ("_instance", "_instance",extensionelement.ExtensionElement, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind",extensionelement.ExtensionElement, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
            ("outputProfile", "outputProfile", str, False, None, False),
            ("_outputProfile", "_outputProfile",extensionelement.ExtensionElement, True, None, False),
            ("overload", "overload", OperationDefinitionOverload, True, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",extensionelement.ExtensionElement, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",extensionelement.ExtensionElement, True, None, False),
            ("resource", "resource", str, True, None, False),
            ("_resource", "_resource",extensionelement.ExtensionElement, True, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",extensionelement.ExtensionElement, True, None, False),
            ("system", "system", bool, False, None, True),
            ("_system", "_system",extensionelement.ExtensionElement, True, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",extensionelement.ExtensionElement, True, None, False),
            ("type", "type", bool, False, None, True),
            ("_type", "_type",extensionelement.ExtensionElement, True, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",extensionelement.ExtensionElement, True, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


from . import backboneelement

class OperationDefinitionOverload(backboneelement.BackboneElement):
    """ Define overloaded variants for when  generating code.
    
    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """
    
    resource_type = "OperationDefinitionOverload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        
        """ Comments to go on overload.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.parameterName = None
        
        """ Name of parameter to include in overload.
        List of `str` items. """
        
        self._parameterName = None
        
        """ extension for fhir primitive  parameterName"""
        
        super(OperationDefinitionOverload, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionOverload, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",extensionelement.ExtensionElement, True, None, False),
            ("parameterName", "parameterName", str, True, None, False),
            ("_parameterName", "_parameterName",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.
    
    The parameters for the operation/query.
    """
    
    resource_type = "OperationDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.binding = None
        
        """ ValueSet details if this is coded.
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """
        
        self.documentation = None
        
        """ Description of meaning/use.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.max = None
        
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self._max = None
        
        """ extension for fhir primitive  max"""
        
        self.min = None
        
        """ Minimum Cardinality.
        Type `int`. """
        
        self._min = None
        
        """ extension for fhir primitive  min"""
        
        self.name = None
        
        """ Name in Parameters.parameter.name or in URL.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.part = None
        
        """ Parts of a nested Parameter.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.referencedFrom = None
        
        """ References to this parameter.
        List of `OperationDefinitionParameterReferencedFrom` items (represented as `dict` in JSON). """
        
        self.searchType = None
        
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        
        self._searchType = None
        
        """ extension for fhir primitive  searchType"""
        
        self.targetProfile = None
        
        """ If type is Reference | canonical, allowed targets.
        List of `str` items. """
        
        self._targetProfile = None
        
        """ extension for fhir primitive  targetProfile"""
        
        self.type = None
        
        """ What type this parameter has.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.use = None
        
        """ in | out.
        Type `str`. """
        
        self._use = None
        
        """ extension for fhir primitive  use"""
        
        super(OperationDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
            ("max", "max", str, False, None, True),
            ("_max", "_max",extensionelement.ExtensionElement, True, None, False),
            ("min", "min", int, False, None, True),
            ("_min", "_min",extensionelement.ExtensionElement, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
            ("part", "part", OperationDefinitionParameter, True, None, False),
            ("referencedFrom", "referencedFrom", OperationDefinitionParameterReferencedFrom, True, None, False),
            ("searchType", "searchType", str, False, None, False),
            ("_searchType", "_searchType",extensionelement.ExtensionElement, True, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("_targetProfile", "_targetProfile",extensionelement.ExtensionElement, True, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",extensionelement.ExtensionElement, True, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_type = "OperationDefinitionParameterBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.strength = None
        
        """ required | extensible | preferred | example.
        Type `str`. """
        
        self._strength = None
        
        """ extension for fhir primitive  strength"""
        
        self.valueSet = None
        
        """ Source of value set.
        Type `str`. """
        
        self._valueSet = None
        
        """ extension for fhir primitive  valueSet"""
        
        super(OperationDefinitionParameterBinding, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("_strength", "_strength",extensionelement.ExtensionElement, True, None, False),
            ("valueSet", "valueSet", str, False, None, True),
            ("_valueSet", "_valueSet",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """ References to this parameter.
    
    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """
    
    resource_type = "OperationDefinitionParameterReferencedFrom"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        
        """ Referencing parameter.
        Type `str`. """
        
        self._source = None
        
        """ extension for fhir primitive  source"""
        
        self.sourceId = None
        
        """ Element id of reference.
        Type `str`. """
        
        self._sourceId = None
        
        """ extension for fhir primitive  sourceId"""
        
        super(OperationDefinitionParameterReferencedFrom, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(OperationDefinitionParameterReferencedFrom, self).elementProperties()
        js.extend([
            ("source", "source", str, False, None, True),
            ("_source", "_source",extensionelement.ExtensionElement, True, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("_sourceId", "_sourceId",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import usagecontext
from . import fhirprimitive

