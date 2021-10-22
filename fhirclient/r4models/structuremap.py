#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class StructureMap(domainresource.DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """
    
    resource_type = "StructureMap"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        """ Natural language description of the structure map.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.group = None
        
        """ Named sections for reader convenience.
        List of `StructureMapGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Additional identifier for the structure map.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.import_fhir = None
        
        """ Other maps used by this map (canonical URLs).
        List of `str` items. """
        
        self._import_fhir = None
        
        """ extension for fhir primitive  import_fhir"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for structure map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this structure map (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this structure map is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.structure = None
        
        """ Structure Definition used by this map.
        List of `StructureMapStructure` items (represented as `dict` in JSON). """
        
        self.title = None
        
        """ Name for this structure map (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Canonical identifier for this structure map, represented as a URI
        (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the structure map.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(StructureMap, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",fhirprimitive.FHIRPrimitive, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",fhirprimitive.FHIRPrimitive, False, None, False),
            ("group", "group", StructureMapGroup, True, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("_import_fhir", "_import",fhirprimitive.FHIRPrimitive, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("structure", "structure", StructureMapStructure, True, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.
    
    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """
    
    resource_type = "StructureMapGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        
        """ Additional description/explanation for group.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.extends = None
        
        """ Another group that this group adds rules to.
        Type `str`. """
        
        self._extends = None
        
        """ extension for fhir primitive  extends"""
        
        self.input = None
        
        """ Named instance provided when invoking the map.
        List of `StructureMapGroupInput` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Human-readable label.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.rule = None
        
        """ Transform Rule from source to target.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        self.typeMode = None
        
        """ none | types | type-and-types.
        Type `str`. """
        
        self._typeMode = None
        
        """ extension for fhir primitive  typeMode"""
        
        super(StructureMapGroup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("extends", "extends", str, False, None, False),
            ("_extends", "_extends",fhirprimitive.FHIRPrimitive, False, None, False),
            ("input", "input", StructureMapGroupInput, True, None, True),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("rule", "rule", StructureMapGroupRule, True, None, True),
            ("typeMode", "typeMode", str, False, None, True),
            ("_typeMode", "_typeMode",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class StructureMapGroupInput(backboneelement.BackboneElement):
    """ Named instance provided when invoking the map.
    
    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """
    
    resource_type = "StructureMapGroupInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        
        """ Documentation for this instance of data.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.mode = None
        
        """ source | target.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.name = None
        
        """ Name for this instance of data.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.type = None
        
        """ Type for this instance of data.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(StructureMapGroupInput, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class StructureMapGroupRule(backboneelement.BackboneElement):
    """ Transform Rule from source to target.
    """
    
    resource_type = "StructureMapGroupRule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dependent = None
        
        """ Which other rules to apply in the context of this rule.
        List of `StructureMapGroupRuleDependent` items (represented as `dict` in JSON). """
        
        self.documentation = None
        
        """ Documentation for this instance of data.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.name = None
        
        """ Name of the rule for internal references.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.rule = None
        
        """ Rules contained in this rule.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        self.source = None
        
        """ Source inputs to the mapping.
        List of `StructureMapGroupRuleSource` items (represented as `dict` in JSON). """
        
        self.target = None
        
        """ Content to create because of this mapping rule.
        List of `StructureMapGroupRuleTarget` items (represented as `dict` in JSON). """
        
        super(StructureMapGroupRule, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("rule", "rule", StructureMapGroupRule, True, None, False),
            ("source", "source", StructureMapGroupRuleSource, True, None, True),
            ("target", "target", StructureMapGroupRuleTarget, True, None, False),
        ])
        return js


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """
    
    resource_type = "StructureMapGroupRuleDependent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        
        """ Name of a rule or group to apply.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.variable = None
        
        """ Variable to pass to the rule or group.
        List of `str` items. """
        
        self._variable = None
        
        """ extension for fhir primitive  variable"""
        
        super(StructureMapGroupRuleDependent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("variable", "variable", str, True, None, True),
            ("_variable", "_variable",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ Source inputs to the mapping.
    """
    
    resource_type = "StructureMapGroupRuleSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.check = None
        
        """ FHIRPath expression  - must be true or the mapping engine throws an
        error instead of completing.
        Type `str`. """
        
        self._check = None
        
        """ extension for fhir primitive  check"""
        
        self.condition = None
        
        """ FHIRPath expression  - must be true or the rule does not apply.
        Type `str`. """
        
        self._condition = None
        
        """ extension for fhir primitive  condition"""
        
        self.context = None
        
        """ Type or variable this rule applies to.
        Type `str`. """
        
        self._context = None
        
        """ extension for fhir primitive  context"""
        
        self.defaultValueAddress = None
        
        """ Default value if no value exists.
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAge = None
        
        """ Default value if no value exists.
        Type `Age` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation = None
        
        """ Default value if no value exists.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment = None
        
        """ Default value if no value exists.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueBase64Binary = None
        
        """ extension for fhir primitive  defaultValueBase64Binary"""
        
        self.defaultValueBoolean = None
        
        """ Default value if no value exists.
        Type `bool`. """
        
        self._defaultValueBoolean = None
        
        """ extension for fhir primitive  defaultValueBoolean"""
        
        self.defaultValueCanonical = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueCanonical = None
        
        """ extension for fhir primitive  defaultValueCanonical"""
        
        self.defaultValueCode = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueCode = None
        
        """ extension for fhir primitive  defaultValueCode"""
        
        self.defaultValueCodeableConcept = None
        
        """ Default value if no value exists.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding = None
        
        """ Default value if no value exists.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactDetail = None
        
        """ Default value if no value exists.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint = None
        
        """ Default value if no value exists.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueContributor = None
        
        """ Default value if no value exists.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.defaultValueCount = None
        
        """ Default value if no value exists.
        Type `Count` (represented as `dict` in JSON). """
        
        self.defaultValueDataRequirement = None
        
        """ Default value if no value exists.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.defaultValueDate = None
        
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDateTime = None
        
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDecimal = None
        
        """ Default value if no value exists.
        Type `float`. """
        
        self._defaultValueDecimal = None
        
        """ extension for fhir primitive  defaultValueDecimal"""
        
        self.defaultValueDistance = None
        
        """ Default value if no value exists.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.defaultValueDosage = None
        
        """ Default value if no value exists.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.defaultValueDuration = None
        
        """ Default value if no value exists.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.defaultValueExpression = None
        
        """ Default value if no value exists.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.defaultValueHumanName = None
        
        """ Default value if no value exists.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueId = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueId = None
        
        """ extension for fhir primitive  defaultValueId"""
        
        self.defaultValueIdentifier = None
        
        """ Default value if no value exists.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant = None
        
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueInteger = None
        
        """ Default value if no value exists.
        Type `int`. """
        
        self._defaultValueInteger = None
        
        """ extension for fhir primitive  defaultValueInteger"""
        
        self.defaultValueMarkdown = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueMarkdown = None
        
        """ extension for fhir primitive  defaultValueMarkdown"""
        
        self.defaultValueMoney = None
        
        """ Default value if no value exists.
        Type `Money` (represented as `dict` in JSON). """
        
        self.defaultValueOid = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueOid = None
        
        """ extension for fhir primitive  defaultValueOid"""
        
        self.defaultValueParameterDefinition = None
        
        """ Default value if no value exists.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.defaultValuePeriod = None
        
        """ Default value if no value exists.
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValuePositiveInt = None
        
        """ Default value if no value exists.
        Type `int`. """
        
        self._defaultValuePositiveInt = None
        
        """ extension for fhir primitive  defaultValuePositiveInt"""
        
        self.defaultValueQuantity = None
        
        """ Default value if no value exists.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange = None
        
        """ Default value if no value exists.
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio = None
        
        """ Default value if no value exists.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference = None
        
        """ Default value if no value exists.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueRelatedArtifact = None
        
        """ Default value if no value exists.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData = None
        
        """ Default value if no value exists.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature = None
        
        """ Default value if no value exists.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueString = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueString = None
        
        """ extension for fhir primitive  defaultValueString"""
        
        self.defaultValueTime = None
        
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueTiming = None
        
        """ Default value if no value exists.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueTriggerDefinition = None
        
        """ Default value if no value exists.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueUnsignedInt = None
        
        """ Default value if no value exists.
        Type `int`. """
        
        self._defaultValueUnsignedInt = None
        
        """ extension for fhir primitive  defaultValueUnsignedInt"""
        
        self.defaultValueUri = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueUri = None
        
        """ extension for fhir primitive  defaultValueUri"""
        
        self.defaultValueUrl = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueUrl = None
        
        """ extension for fhir primitive  defaultValueUrl"""
        
        self.defaultValueUsageContext = None
        
        """ Default value if no value exists.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.defaultValueUuid = None
        
        """ Default value if no value exists.
        Type `str`. """
        
        self._defaultValueUuid = None
        
        """ extension for fhir primitive  defaultValueUuid"""
        
        self.element = None
        
        """ Optional field for this source.
        Type `str`. """
        
        self._element = None
        
        """ extension for fhir primitive  element"""
        
        self.listMode = None
        
        """ first | not_first | last | not_last | only_one.
        Type `str`. """
        
        self._listMode = None
        
        """ extension for fhir primitive  listMode"""
        
        self.logMessage = None
        
        """ Message to put in log if source exists (FHIRPath).
        Type `str`. """
        
        self._logMessage = None
        
        """ extension for fhir primitive  logMessage"""
        
        self.max = None
        
        """ Specified maximum cardinality (number or *).
        Type `str`. """
        
        self._max = None
        
        """ extension for fhir primitive  max"""
        
        self.min = None
        
        """ Specified minimum cardinality.
        Type `int`. """
        
        self._min = None
        
        """ extension for fhir primitive  min"""
        
        self.type = None
        
        """ Rule only applies if source has this type.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.variable = None
        
        """ Named context for field, if a field is specified.
        Type `str`. """
        
        self._variable = None
        
        """ extension for fhir primitive  variable"""
        
        super(StructureMapGroupRuleSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, False, None, False),
            ("_check", "_check",fhirprimitive.FHIRPrimitive, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("_condition", "_condition",fhirprimitive.FHIRPrimitive, False, None, False),
            ("context", "context", str, False, None, True),
            ("_context", "_context",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("_defaultValueBase64Binary", "_defaultValueBase64Binary",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("_defaultValueBoolean", "_defaultValueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("_defaultValueCanonical", "_defaultValueCanonical",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("_defaultValueCode", "_defaultValueCode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("_defaultValueDecimal", "_defaultValueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("_defaultValueId", "_defaultValueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("_defaultValueInteger", "_defaultValueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("_defaultValueMarkdown", "_defaultValueMarkdown",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("_defaultValueOid", "_defaultValueOid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("_defaultValuePositiveInt", "_defaultValuePositiveInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("_defaultValueString", "_defaultValueString",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("_defaultValueUnsignedInt", "_defaultValueUnsignedInt",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("_defaultValueUri", "_defaultValueUri",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("_defaultValueUrl", "_defaultValueUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("_defaultValueUuid", "_defaultValueUuid",fhirprimitive.FHIRPrimitive, False, None, False),
            ("element", "element", str, False, None, False),
            ("_element", "_element",fhirprimitive.FHIRPrimitive, False, None, False),
            ("listMode", "listMode", str, False, None, False),
            ("_listMode", "_listMode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("logMessage", "logMessage", str, False, None, False),
            ("_logMessage", "_logMessage",fhirprimitive.FHIRPrimitive, False, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max",fhirprimitive.FHIRPrimitive, False, None, False),
            ("min", "min", int, False, None, False),
            ("_min", "_min",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("variable", "variable", str, False, None, False),
            ("_variable", "_variable",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """ Content to create because of this mapping rule.
    """
    
    resource_type = "StructureMapGroupRuleTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context = None
        
        """ Type or variable this rule applies to.
        Type `str`. """
        
        self._context = None
        
        """ extension for fhir primitive  context"""
        
        self.contextType = None
        
        """ type | variable.
        Type `str`. """
        
        self._contextType = None
        
        """ extension for fhir primitive  contextType"""
        
        self.element = None
        
        """ Field to create in the context.
        Type `str`. """
        
        self._element = None
        
        """ extension for fhir primitive  element"""
        
        self.listMode = None
        
        """ first | share | last | collate.
        List of `str` items. """
        
        self._listMode = None
        
        """ extension for fhir primitive  listMode"""
        
        self.listRuleId = None
        
        """ Internal rule reference for shared list items.
        Type `str`. """
        
        self._listRuleId = None
        
        """ extension for fhir primitive  listRuleId"""
        
        self.parameter = None
        
        """ Parameters to the transform.
        List of `StructureMapGroupRuleTargetParameter` items (represented as `dict` in JSON). """
        
        self.transform = None
        
        """ create | copy +.
        Type `str`. """
        
        self._transform = None
        
        """ extension for fhir primitive  transform"""
        
        self.variable = None
        
        """ Named context for field, if desired, and a field is specified.
        Type `str`. """
        
        self._variable = None
        
        """ extension for fhir primitive  variable"""
        
        super(StructureMapGroupRuleTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, False, None, False),
            ("_context", "_context",fhirprimitive.FHIRPrimitive, False, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("_contextType", "_contextType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("element", "element", str, False, None, False),
            ("_element", "_element",fhirprimitive.FHIRPrimitive, False, None, False),
            ("listMode", "listMode", str, True, None, False),
            ("_listMode", "_listMode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("listRuleId", "listRuleId", str, False, None, False),
            ("_listRuleId", "_listRuleId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("_transform", "_transform",fhirprimitive.FHIRPrimitive, False, None, False),
            ("variable", "variable", str, False, None, False),
            ("_variable", "_variable",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ Parameters to the transform.
    """
    
    resource_type = "StructureMapGroupRuleTargetParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueBoolean = None
        
        """ Parameter value - variable or literal.
        Type `bool`. """
        
        self._valueBoolean = None
        
        """ extension for fhir primitive  valueBoolean"""
        
        self.valueDecimal = None
        
        """ Parameter value - variable or literal.
        Type `float`. """
        
        self._valueDecimal = None
        
        """ extension for fhir primitive  valueDecimal"""
        
        self.valueId = None
        
        """ Parameter value - variable or literal.
        Type `str`. """
        
        self._valueId = None
        
        """ extension for fhir primitive  valueId"""
        
        self.valueInteger = None
        
        """ Parameter value - variable or literal.
        Type `int`. """
        
        self._valueInteger = None
        
        """ extension for fhir primitive  valueInteger"""
        
        self.valueString = None
        
        """ Parameter value - variable or literal.
        Type `str`. """
        
        self._valueString = None
        
        """ extension for fhir primitive  valueString"""
        
        super(StructureMapGroupRuleTargetParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger",fhirprimitive.FHIRPrimitive, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class StructureMapStructure(backboneelement.BackboneElement):
    """ Structure Definition used by this map.
    
    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """
    
    resource_type = "StructureMapStructure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        
        """ Name for type in this map.
        Type `str`. """
        
        self._alias = None
        
        """ extension for fhir primitive  alias"""
        
        self.documentation = None
        
        """ Documentation on use of structure.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.mode = None
        
        """ source | queried | target | produced.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.url = None
        
        """ Canonical reference to structure definition.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        super(StructureMapStructure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, False, None, False),
            ("_alias", "_alias",fhirprimitive.FHIRPrimitive, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext
from . import fhirprimitive

