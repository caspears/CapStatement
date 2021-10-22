#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource
from . import element
from . import extensionelement

class CapabilityStatement(domainresource.DomainResource):
    """ A statement of system capabilities.
    
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    
    resource_type = "CapabilityStatement"
    
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
        
        """ Natural language description of the capability statement.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.document = None
        
        """ Document definition.
        List of `CapabilityStatementDocument` items (represented as `dict` in JSON). """
        
        self.experimental = None
        
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self._experimental = None
        
        """ extension for fhir primitive  experimental"""
        
        self.fhirVersion = None
        
        """ FHIR Version the system supports.
        Type `str`. """
        
        self._fhirVersion = None
        
        """ extension for fhir primitive  fhirVersion"""
        
        self.format = None
        
        """ formats supported (xml | json | ttl | mime type).
        List of `str` items. """
        
        self._format = None
        
        """ extension for fhir primitive  format"""
        
        self.implementation = None
        
        """ If this describes a specific instance.
        Type `CapabilityStatementImplementation` (represented as `dict` in JSON). """
        
        self.implementationGuide = None
        
        """ Implementation guides supported.
        List of `str` items. """
        
        self._implementationGuide = None
        
        """ extension for fhir primitive  implementationGuide"""
        
        self.imports = None
        
        """ Canonical URL of another capability statement this adds to.
        List of `str` items. """
        
        self._imports = None
        
        """ extension for fhir primitive  imports"""
        
        self.instantiates = None
        
        """ Canonical URL of another capability statement this implements.
        List of `str` items. """
        
        self._instantiates = None
        
        """ extension for fhir primitive  instantiates"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for capability statement (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        
        """ instance | capability | requirements.
        Type `str`. """
        
        self._kind = None
        
        """ extension for fhir primitive  kind"""
        
        self.messaging = None
        
        """ If messaging is supported.
        List of `CapabilityStatementMessaging` items (represented as `dict` in JSON). """
        
        self.name = None
        
        """ Name for this capability statement (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.patchFormat = None
        
        """ Patch formats supported.
        List of `str` items. """
        
        self._patchFormat = None
        
        """ extension for fhir primitive  patchFormat"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.purpose = None
        
        """ Why this capability statement is defined.
        Type `str`. """
        
        self._purpose = None
        
        """ extension for fhir primitive  purpose"""
        
        self.rest = None
        
        """ If the endpoint is a RESTful one.
        List of `CapabilityStatementRest` items (represented as `dict` in JSON). """
        
        self.software = None
        
        """ Software that is covered by this capability statement.
        Type `CapabilityStatementSoftware` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.title = None
        
        """ Name for this capability statement (human friendly).
        Type `str`. """
        
        self._title = None
        
        """ extension for fhir primitive  title"""
        
        self.url = None
        
        """ Canonical identifier for this capability statement, represented as
        a URI (globally unique).
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        
        """ Business version of the capability statement.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(CapabilityStatement, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatement, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright",extensionelement.ExtensionElement, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("_description", "_description",extensionelement.ExtensionElement, True, None, False),
            ("document", "document", CapabilityStatementDocument, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental",extensionelement.ExtensionElement, True, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("_fhirVersion", "_fhirVersion",extensionelement.ExtensionElement, True, None, False),
            ("format", "format", str, True, None, True),
            ("_format", "_format",extensionelement.ExtensionElement, True, None, False),
            ("implementation", "implementation", CapabilityStatementImplementation, False, None, False),
            ("implementationGuide", "implementationGuide", str, True, None, False),
            ("_implementationGuide", "_implementationGuide",extensionelement.ExtensionElement, True, None, False),
            ("imports", "imports", str, True, None, False),
            ("_imports", "_imports",extensionelement.ExtensionElement, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("_instantiates", "_instantiates",extensionelement.ExtensionElement, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind",extensionelement.ExtensionElement, True, None, False),
            ("messaging", "messaging", CapabilityStatementMessaging, True, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
            ("patchFormat", "patchFormat", str, True, None, False),
            ("_patchFormat", "_patchFormat",extensionelement.ExtensionElement, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",extensionelement.ExtensionElement, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose",extensionelement.ExtensionElement, True, None, False),
            ("rest", "rest", CapabilityStatementRest, True, None, False),
            ("software", "software", CapabilityStatementSoftware, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",extensionelement.ExtensionElement, True, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title",extensionelement.ExtensionElement, True, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",extensionelement.ExtensionElement, True, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


from . import backboneelement

class CapabilityStatementDocument(backboneelement.BackboneElement):
    """ Document definition.
    
    A document definition.
    """
    
    resource_type = "CapabilityStatementDocument"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        
        """ Description of document support.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.mode = None
        
        """ producer | consumer.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.profile = None
        
        """ Constraint on the resources used in the document.
        Type `str`. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        super(CapabilityStatementDocument, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementDocument, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode",extensionelement.ExtensionElement, True, None, False),
            ("profile", "profile", str, False, None, True),
            ("_profile", "_profile",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    
    resource_type = "CapabilityStatementImplementation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.custodian = None
        
        """ Organization that manages the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.description = None
        
        """ Describes this specific instance.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.url = None
        
        """ Base URL for the installation.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        super(CapabilityStatementImplementation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementImplementation, self).elementProperties()
        js.extend([
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, True),
            ("_description", "_description",extensionelement.ExtensionElement, True, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """ If messaging is supported.
    
    A description of the messaging capabilities of the solution.
    """
    
    resource_type = "CapabilityStatementMessaging"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        
        """ Messaging interface behavior details.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.endpoint = None
        
        """ Where messages should be sent.
        List of `CapabilityStatementMessagingEndpoint` items (represented as `dict` in JSON). """
        
        self.reliableCache = None
        
        """ Reliable Message Cache Length (min).
        Type `int`. """
        
        self._reliableCache = None
        
        """ extension for fhir primitive  reliableCache"""
        
        self.supportedMessage = None
        
        """ Messages supported by this system.
        List of `CapabilityStatementMessagingSupportedMessage` items (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessaging, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementMessaging, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
            ("endpoint", "endpoint", CapabilityStatementMessagingEndpoint, True, None, False),
            ("reliableCache", "reliableCache", int, False, None, False),
            ("_reliableCache", "_reliableCache",extensionelement.ExtensionElement, True, None, False),
            ("supportedMessage", "supportedMessage", CapabilityStatementMessagingSupportedMessage, True, None, False),
        ])
        return js


class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """ Where messages should be sent.
    
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    
    resource_type = "CapabilityStatementMessagingEndpoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        
        """ Network address or identifier of the end-point.
        Type `str`. """
        
        self._address = None
        
        """ extension for fhir primitive  address"""
        
        self.protocol = None
        
        """ http | ftp | mllp +.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessagingEndpoint, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementMessagingEndpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("_address", "_address",extensionelement.ExtensionElement, True, None, False),
            ("protocol", "protocol", coding.Coding, False, None, True),
        ])
        return js


class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """ Messages supported by this system.
    
    References to message definitions for messages this system can send or
    receive.
    """
    
    resource_type = "CapabilityStatementMessagingSupportedMessage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        
        """ Message supported by this system.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.mode = None
        
        """ sender | receiver.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        super(CapabilityStatementMessagingSupportedMessage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementMessagingSupportedMessage, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("_definition", "_definition",extensionelement.ExtensionElement, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementRest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    resource_type = "CapabilityStatementRest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        
        """ Compartments served/used by system.
        List of `str` items. """
        
        self._compartment = None
        
        """ extension for fhir primitive  compartment"""
        
        self.documentation = None
        
        """ General description of implementation.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.interaction = None
        
        """ What operations are supported?.
        List of `CapabilityStatementRestInteraction` items (represented as `dict` in JSON). """
        
        self.mode = None
        
        """ client | server.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.operation = None
        
        """ Definition of a system level operation.
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        
        self.resource = None
        
        """ Resource served on the REST interface.
        List of `CapabilityStatementRestResource` items (represented as `dict` in JSON). """
        
        self.searchParam = None
        
        """ Search parameters for searching all resources.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.security = None
        
        """ Information about security of implementation.
        Type `CapabilityStatementRestSecurity` (represented as `dict` in JSON). """
        
        super(CapabilityStatementRest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", str, True, None, False),
            ("_compartment", "_compartment",extensionelement.ExtensionElement, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
            ("interaction", "interaction", CapabilityStatementRestInteraction, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode",extensionelement.ExtensionElement, True, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("resource", "resource", CapabilityStatementRestResource, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("security", "security", CapabilityStatementRestSecurity, False, None, False),
        ])
        return js


class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    A specification of restful operations supported by the system.
    """
    
    resource_type = "CapabilityStatementRestInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ transaction | batch | search-system | history-system.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.documentation = None
        
        """ Anything special about operation behavior.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        super(CapabilityStatementRestInteraction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",extensionelement.ExtensionElement, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    resource_type = "CapabilityStatementRestResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conditionalCreate = None
        
        """ If allows/uses conditional create.
        Type `bool`. """
        
        self._conditionalCreate = None
        
        """ extension for fhir primitive  conditionalCreate"""
        
        self.conditionalDelete = None
        
        """ not-supported | single | multiple - how conditional delete is
        supported.
        Type `str`. """
        
        self._conditionalDelete = None
        
        """ extension for fhir primitive  conditionalDelete"""
        
        self.conditionalRead = None
        
        """ not-supported | modified-since | not-match | full-support.
        Type `str`. """
        
        self._conditionalRead = None
        
        """ extension for fhir primitive  conditionalRead"""
        
        self.conditionalUpdate = None
        
        """ If allows/uses conditional update.
        Type `bool`. """
        
        self._conditionalUpdate = None
        
        """ extension for fhir primitive  conditionalUpdate"""
        
        self.documentation = None
        
        """ Additional information about the use of the resource type.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.interaction = None
        
        """ What operations are supported?.
        List of `CapabilityStatementRestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.operation = None
        
        """ Definition of a resource operation.
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        
        self.profile = None
        
        """ Base System profile for all uses of resource.
        Type `str`. """
        
        self._profile = None
        
        """ extension for fhir primitive  profile"""
        
        self.readHistory = None
        
        """ Whether vRead can return past versions.
        Type `bool`. """
        
        self._readHistory = None
        
        """ extension for fhir primitive  readHistory"""
        
        self.referencePolicy = None
        
        """ literal | logical | resolves | enforced | local.
        List of `str` items. """
        
        self._referencePolicy = None
        
        """ extension for fhir primitive  referencePolicy"""
        
        self.searchInclude = None
        
        """ _include values supported by the server.
        List of `str` items. """
        
        self._searchInclude = None
        
        """ extension for fhir primitive  searchInclude"""
        
        self.searchParam = None
        
        """ Search parameters supported by implementation.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.searchRevInclude = None
        
        """ _revinclude values supported by the server.
        List of `str` items. """
        
        self._searchRevInclude = None
        
        """ extension for fhir primitive  searchRevInclude"""
        
        self.supportedProfile = None
        
        """ Profiles for use cases supported.
        List of `str` items. """
        
        self._supportedProfile = None
        
        """ extension for fhir primitive  supportedProfile"""
        
        self.type = None
        
        """ A resource type that is supported.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.updateCreate = None
        
        """ If update can commit to a new identity.
        Type `bool`. """
        
        self._updateCreate = None
        
        """ extension for fhir primitive  updateCreate"""
        
        self.versioning = None
        
        """ no-version | versioned | versioned-update.
        Type `str`. """
        
        self._versioning = None
        
        """ extension for fhir primitive  versioning"""
        
        super(CapabilityStatementRestResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResource, self).elementProperties()
        js.extend([
            ("conditionalCreate", "conditionalCreate", bool, False, None, False),
            ("_conditionalCreate", "_conditionalCreate",extensionelement.ExtensionElement, True, None, False),
            ("conditionalDelete", "conditionalDelete", str, False, None, False),
            ("_conditionalDelete", "_conditionalDelete",extensionelement.ExtensionElement, True, None, False),
            ("conditionalRead", "conditionalRead", str, False, None, False),
            ("_conditionalRead", "_conditionalRead",extensionelement.ExtensionElement, True, None, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False, None, False),
            ("_conditionalUpdate", "_conditionalUpdate",extensionelement.ExtensionElement, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
            ("interaction", "interaction", CapabilityStatementRestResourceInteraction, True, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile",extensionelement.ExtensionElement, True, None, False),
            ("readHistory", "readHistory", bool, False, None, False),
            ("_readHistory", "_readHistory",extensionelement.ExtensionElement, True, None, False),
            ("referencePolicy", "referencePolicy", str, True, None, False),
            ("_referencePolicy", "_referencePolicy",extensionelement.ExtensionElement, True, None, False),
            ("searchInclude", "searchInclude", str, True, None, False),
            ("_searchInclude", "_searchInclude",extensionelement.ExtensionElement, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("searchRevInclude", "searchRevInclude", str, True, None, False),
            ("_searchRevInclude", "_searchRevInclude",extensionelement.ExtensionElement, True, None, False),
            ("supportedProfile", "supportedProfile", str, True, None, False),
            ("_supportedProfile", "_supportedProfile",extensionelement.ExtensionElement, True, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",extensionelement.ExtensionElement, True, None, False),
            ("updateCreate", "updateCreate", bool, False, None, False),
            ("_updateCreate", "_updateCreate",extensionelement.ExtensionElement, True, None, False),
            ("versioning", "versioning", str, False, None, False),
            ("_versioning", "_versioning",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    Identifies a restful operation supported by the solution.
    """
    
    resource_type = "CapabilityStatementRestResourceInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ read | vread | update | patch | delete | history-instance |
        history-type | create | search-type.
        Type `str`. """
        
        self._code = None
        
        """ extension for fhir primitive  code"""
        
        self.documentation = None
        
        """ Anything special about operation behavior.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        super(CapabilityStatementRestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code",extensionelement.ExtensionElement, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementRestResourceOperation(backboneelement.BackboneElement):
    """ Definition of a resource operation.
    
    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    
    resource_type = "CapabilityStatementRestResourceOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        
        """ The defined operation/query.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.documentation = None
        
        """ Specific details about operation behavior.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.name = None
        
        """ Name by which the operation/query is invoked.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        super(CapabilityStatementRestResourceOperation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("_definition", "_definition",extensionelement.ExtensionElement, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search parameters supported by implementation.
    
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    
    resource_type = "CapabilityStatementRestResourceSearchParam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        
        """ Source of definition for parameter.
        Type `str`. """
        
        self._definition = None
        
        """ extension for fhir primitive  definition"""
        
        self.documentation = None
        
        """ Server-specific usage.
        Type `str`. """
        
        self._documentation = None
        
        """ extension for fhir primitive  documentation"""
        
        self.name = None
        
        """ Name of search parameter.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.type = None
        
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(CapabilityStatementRestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition",extensionelement.ExtensionElement, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation",extensionelement.ExtensionElement, True, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """ Information about security of implementation.
    
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    
    resource_type = "CapabilityStatementRestSecurity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cors = None
        
        """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """
        
        self._cors = None
        
        """ extension for fhir primitive  cors"""
        
        self.description = None
        
        """ General description of how security works.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.service = None
        
        """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(CapabilityStatementRestSecurity, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementRestSecurity, self).elementProperties()
        js.extend([
            ("cors", "cors", bool, False, None, False),
            ("_cors", "_cors",extensionelement.ExtensionElement, True, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description",extensionelement.ExtensionElement, True, None, False),
            ("service", "service", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this capability statement.
    
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    
    resource_type = "CapabilityStatementSoftware"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        
        """ A name the software is known by.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.releaseDate = None
        
        """ Date this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.version = None
        
        """ Version covered by this statement.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(CapabilityStatementSoftware, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CapabilityStatementSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name",extensionelement.ExtensionElement, True, None, False),
            ("releaseDate", "releaseDate", fhirdate.FHIRDate, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version",extensionelement.ExtensionElement, True, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext
from . import fhirprimitive

