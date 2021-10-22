#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Device) on 2018-12-20.
#  2018, SMART Health IT.


from . import domainresource

class Device(domainresource.DomainResource):
    """ Item used in healthcare.
    
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """
    
    resource_type = "Device"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.definition = None
        
        """ The reference to the definition for the device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deviceName = None
        
        """ The name of the device as given by the manufacturer.
        List of `DeviceDeviceName` items (represented as `dict` in JSON). """
        
        self.distinctIdentifier = None
        
        """ The distinct identification string.
        Type `str`. """
        
        self._distinctIdentifier = None
        
        """ extension for fhir primitive  distinctIdentifier"""
        
        self.expirationDate = None
        
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        
        """ Where the device is found.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        
        """ Lot number of manufacture.
        Type `str`. """
        
        self._lotNumber = None
        
        """ extension for fhir primitive  lotNumber"""
        
        self.manufactureDate = None
        
        """ Date when the device was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.manufacturer = None
        
        """ Name of device manufacturer.
        Type `str`. """
        
        self._manufacturer = None
        
        """ extension for fhir primitive  manufacturer"""
        
        self.modelNumber = None
        
        """ The model number for the device.
        Type `str`. """
        
        self._modelNumber = None
        
        """ extension for fhir primitive  modelNumber"""
        
        self.note = None
        
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.owner = None
        
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parent = None
        
        """ The parent device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partNumber = None
        
        """ The part number of the device.
        Type `str`. """
        
        self._partNumber = None
        
        """ extension for fhir primitive  partNumber"""
        
        self.patient = None
        
        """ Patient to whom Device is affixed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.property = None
        
        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
        List of `DeviceProperty` items (represented as `dict` in JSON). """
        
        self.safety = None
        
        """ Safety Characteristics of Device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serialNumber = None
        
        """ Serial number assigned by the manufacturer.
        Type `str`. """
        
        self._serialNumber = None
        
        """ extension for fhir primitive  serialNumber"""
        
        self.specialization = None
        
        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
        List of `DeviceSpecialization` items (represented as `dict` in JSON). """
        
        self.status = None
        
        """ active | inactive | entered-in-error | unknown.
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        self.statusReason = None
        
        """ online | paused | standby | offline | not-ready | transduc-discon |
        hw-discon | off.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        
        """ The kind or type of device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udiCarrier = None
        
        """ Unique Device Identifier (UDI) Barcode string.
        List of `DeviceUdiCarrier` items (represented as `dict` in JSON). """
        
        self.url = None
        
        """ Network address to contact device.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        self.version = None
        
        """ The actual design of the device or software version running on the
        device.
        List of `DeviceVersion` items (represented as `dict` in JSON). """
        
        super(Device, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("definition", "definition", fhirreference.FHIRReference, False, None, False),
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False),
            ("distinctIdentifier", "distinctIdentifier", str, False, None, False),
            ("_distinctIdentifier", "_distinctIdentifier",fhirprimitive.FHIRPrimitive, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("_lotNumber", "_lotNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("_manufacturer", "_manufacturer",fhirprimitive.FHIRPrimitive, False, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("_modelNumber", "_modelNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("partNumber", "partNumber", str, False, None, False),
            ("_partNumber", "_partNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("property", "property", DeviceProperty, True, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("_serialNumber", "_serialNumber",fhirprimitive.FHIRPrimitive, False, None, False),
            ("specialization", "specialization", DeviceSpecialization, True, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
            ("version", "version", DeviceVersion, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceDeviceName(backboneelement.BackboneElement):
    """ The name of the device as given by the manufacturer.
    
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """
    
    resource_type = "DeviceDeviceName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        
        """ The name of the device.
        Type `str`. """
        
        self._name = None
        
        """ extension for fhir primitive  name"""
        
        self.type = None
        
        """ udi-label-name | user-friendly-name | patient-reported-name |
        manufacturer-name | model-name | other.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(DeviceDeviceName, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class DeviceProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    
    resource_type = "DeviceProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        
        """ Code that specifies the property DeviceDefinitionPropetyCode
        (Extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCode = None
        
        """ Property value as a code, e.g., NTP4 (synced to NTP).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        
        """ Property value as a quantity.
        List of `Quantity` items (represented as `dict` in JSON). """
        
        super(DeviceProperty, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
        ])
        return js


class DeviceSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    
    resource_type = "DeviceSpecialization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.systemType = None
        
        """ The standard that is used to operate and communicate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.version = None
        
        """ The version of the standard that is used to operate and communicate.
        Type `str`. """
        
        self._version = None
        
        """ extension for fhir primitive  version"""
        
        super(DeviceSpecialization, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", codeableconcept.CodeableConcept, False, None, True),
            ("version", "version", str, False, None, False),
            ("_version", "_version",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    
    resource_type = "DeviceUdiCarrier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.carrierAIDC = None
        
        """ UDI Machine Readable Barcode String.
        Type `str`. """
        
        self._carrierAIDC = None
        
        """ extension for fhir primitive  carrierAIDC"""
        
        self.carrierHRF = None
        
        """ UDI Human Readable Barcode String.
        Type `str`. """
        
        self._carrierHRF = None
        
        """ extension for fhir primitive  carrierHRF"""
        
        self.deviceIdentifier = None
        
        """ Mandatory fixed portion of UDI.
        Type `str`. """
        
        self._deviceIdentifier = None
        
        """ extension for fhir primitive  deviceIdentifier"""
        
        self.entryType = None
        
        """ barcode | rfid | manual +.
        Type `str`. """
        
        self._entryType = None
        
        """ extension for fhir primitive  entryType"""
        
        self.issuer = None
        
        """ UDI Issuing Organization.
        Type `str`. """
        
        self._issuer = None
        
        """ extension for fhir primitive  issuer"""
        
        self.jurisdiction = None
        
        """ Regional UDI authority.
        Type `str`. """
        
        self._jurisdiction = None
        
        """ extension for fhir primitive  jurisdiction"""
        
        super(DeviceUdiCarrier, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceUdiCarrier, self).elementProperties()
        js.extend([
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("_carrierAIDC", "_carrierAIDC",fhirprimitive.FHIRPrimitive, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("_carrierHRF", "_carrierHRF",fhirprimitive.FHIRPrimitive, False, None, False),
            ("deviceIdentifier", "deviceIdentifier", str, False, None, False),
            ("_deviceIdentifier", "_deviceIdentifier",fhirprimitive.FHIRPrimitive, False, None, False),
            ("entryType", "entryType", str, False, None, False),
            ("_entryType", "_entryType",fhirprimitive.FHIRPrimitive, False, None, False),
            ("issuer", "issuer", str, False, None, False),
            ("_issuer", "_issuer",fhirprimitive.FHIRPrimitive, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, False),
            ("_jurisdiction", "_jurisdiction",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class DeviceVersion(backboneelement.BackboneElement):
    """ The actual design of the device or software version running on the device.
    """
    
    resource_type = "DeviceVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.component = None
        
        """ A single component of the device version.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        
        """ The type of the device version.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        
        """ The version text.
        Type `str`. """
        
        self._value = None
        
        """ extension for fhir primitive  value"""
        
        super(DeviceVersion, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("component", "component", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import fhirprimitive

