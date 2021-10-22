#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.
    
    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    
    resource_type = "NamingSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        
        """ Natural language description of the naming system.
        Type `str`. """
        
        self._description = None
        
        """ extension for fhir primitive  description"""
        
        self.jurisdiction = None
        
        """ Intended jurisdiction for naming system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        
        """ codesystem | identifier | root.
        Type `str`. """
        
        self._kind = None
        
        """ extension for fhir primitive  kind"""
        
        self.name = None
        
        """ Name for this naming system (computer friendly).
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.publisher = None
        
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self._publisher = None
        
        """ extension for fhir primitive  publisher"""
        
        self.responsible = None
        
        """ Who maintains system namespace?.
        Type `str`. """
        
        self._responsible = None
        
        """ extension for fhir primitive  responsible"""
        
        self.status = None
        
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.type = None
        
        """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uniqueId = None
        
        """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """
        
        self.usage = None
        
        """ How/where is it used.
        Type `str`. """
        
        self._usage = None
        
        """ extension for fhir primitive  usage"""
        
        self.useContext = None
        
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        super(NamingSystem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("_description", "_description",fhirprimitive.FHIRPrimitive, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind",fhirprimitive.FHIRPrimitive, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher",fhirprimitive.FHIRPrimitive, False, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("_responsible", "_responsible",fhirprimitive.FHIRPrimitive, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage",fhirprimitive.FHIRPrimitive, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


from . import backboneelement

class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.
    
    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    
    resource_type = "NamingSystemUniqueId"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        
        """ Notes about identifier usage.
        Type `str`. """
        
        self._comment = None
        
        """ extension for fhir primitive  comment"""
        
        self.period = None
        
        """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """
        
        self.preferred = None
        
        """ Is this the id that should be used for this type.
        Type `bool`. """
        
        self._preferred = None
        
        """ extension for fhir primitive  preferred"""
        
        self.type = None
        
        """ oid | uuid | uri | other.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        self.value = None
        
        """ The unique identifier.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(NamingSystemUniqueId, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment",fhirprimitive.FHIRPrimitive, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("_preferred", "_preferred",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import period
from . import usagecontext
from . import fhirprimitive

