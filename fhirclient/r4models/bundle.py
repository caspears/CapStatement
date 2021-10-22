#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Bundle) on 2018-12-20.
#  2018, SMART Health IT.


from . import resource

class Bundle(resource.Resource):
    """ Contains a collection of resources.
    
    A container for a collection of resources.
    """
    
    resource_type = "Bundle"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entry = None
        
        """ Entry in the bundle - will have a resource or information.
        List of `BundleEntry` items (represented as `dict` in JSON). """
        
        self.identifier = None
        
        """ Persistent identifier for the bundle.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.link = None
        
        """ Links related to this Bundle.
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.signature = None
        
        """ Digital Signature.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.timestamp = None
        
        """ When the bundle was assembled.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.total = None
        
        """ If search, the total number of matches.
        Type `int`. """
        
        self._total = None
        
        """ extension for fhir primitive  total"""
        
        self.type = None
        
        """ document | message | transaction | transaction-response | batch |
        batch-response | history | searchset | collection.
        Type `str`. """
        
        self._type = None
        
        """ extension for fhir primitive  type"""
        
        super(Bundle, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Bundle, self).elementProperties()
        js.extend([
            ("entry", "entry", BundleEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("signature", "signature", signature.Signature, False, None, False),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, False),
            ("total", "total", int, False, None, False),
            ("_total", "_total",fhirprimitive.FHIRPrimitive, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import backboneelement

class BundleEntry(backboneelement.BackboneElement):
    """ Entry in the bundle - will have a resource or information.
    
    An entry in a bundle resource - will either contain a resource or
    information about a resource (transactions and history only).
    """
    
    resource_type = "BundleEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fullUrl = None
        
        """ URI for resource (Absolute URL server address or URI for UUID/OID).
        Type `str`. """
        
        self._fullUrl = None
        
        """ extension for fhir primitive  fullUrl"""
        
        self.link = None
        
        """ Links related to this entry.
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.request = None
        
        """ Additional execution information (transaction/batch/history).
        Type `BundleEntryRequest` (represented as `dict` in JSON). """
        
        self.resource = None
        
        """ A resource in the bundle.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.response = None
        
        """ Results of execution (transaction/batch/history).
        Type `BundleEntryResponse` (represented as `dict` in JSON). """
        
        self.search = None
        
        """ Search related information.
        Type `BundleEntrySearch` (represented as `dict` in JSON). """
        
        super(BundleEntry, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntry, self).elementProperties()
        js.extend([
            ("fullUrl", "fullUrl", str, False, None, False),
            ("_fullUrl", "_fullUrl",fhirprimitive.FHIRPrimitive, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("request", "request", BundleEntryRequest, False, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("response", "response", BundleEntryResponse, False, None, False),
            ("search", "search", BundleEntrySearch, False, None, False),
        ])
        return js


class BundleEntryRequest(backboneelement.BackboneElement):
    """ Additional execution information (transaction/batch/history).
    
    Additional information about how this entry should be processed as part of
    a transaction or batch.  For history, it shows how the entry was processed
    to create the version contained in the entry.
    """
    
    resource_type = "BundleEntryRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ifMatch = None
        
        """ For managing update contention.
        Type `str`. """
        
        self._ifMatch = None
        
        """ extension for fhir primitive  ifMatch"""
        
        self.ifModifiedSince = None
        
        """ For managing cache currency.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.ifNoneExist = None
        
        """ For conditional creates.
        Type `str`. """
        
        self._ifNoneExist = None
        
        """ extension for fhir primitive  ifNoneExist"""
        
        self.ifNoneMatch = None
        
        """ For managing cache currency.
        Type `str`. """
        
        self._ifNoneMatch = None
        
        """ extension for fhir primitive  ifNoneMatch"""
        
        self.method = None
        
        """ GET | HEAD | POST | PUT | DELETE | PATCH.
        Type `str`. """
        
        self._method = None
        
        """ extension for fhir primitive  method"""
        
        self.url = None
        
        """ URL for HTTP equivalent of this entry.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        super(BundleEntryRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntryRequest, self).elementProperties()
        js.extend([
            ("ifMatch", "ifMatch", str, False, None, False),
            ("_ifMatch", "_ifMatch",fhirprimitive.FHIRPrimitive, False, None, False),
            ("ifModifiedSince", "ifModifiedSince", fhirdate.FHIRDate, False, None, False),
            ("ifNoneExist", "ifNoneExist", str, False, None, False),
            ("_ifNoneExist", "_ifNoneExist",fhirprimitive.FHIRPrimitive, False, None, False),
            ("ifNoneMatch", "ifNoneMatch", str, False, None, False),
            ("_ifNoneMatch", "_ifNoneMatch",fhirprimitive.FHIRPrimitive, False, None, False),
            ("method", "method", str, False, None, True),
            ("_method", "_method",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class BundleEntryResponse(backboneelement.BackboneElement):
    """ Results of execution (transaction/batch/history).
    
    Indicates the results of processing the corresponding 'request' entry in
    the batch or transaction being responded to or what the results of an
    operation where when returning history.
    """
    
    resource_type = "BundleEntryResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.etag = None
        
        """ The Etag for the resource (if relevant).
        Type `str`. """
        
        self._etag = None
        
        """ extension for fhir primitive  etag"""
        
        self.lastModified = None
        
        """ Server's date time modified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.location = None
        
        """ The location (if the operation returns a location).
        Type `str`. """
        
        self._location = None
        
        """ extension for fhir primitive  location"""
        
        self.outcome = None
        
        """ OperationOutcome with hints and warnings (for batch/transaction).
        Type `Resource` (represented as `dict` in JSON). """
        
        self.status = None
        
        """ Status response code (text optional).
        Type `str`. """
        
        self._status = None
        
        """ extension for fhir primitive  status"""
        
        super(BundleEntryResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntryResponse, self).elementProperties()
        js.extend([
            ("etag", "etag", str, False, None, False),
            ("_etag", "_etag",fhirprimitive.FHIRPrimitive, False, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, False),
            ("location", "location", str, False, None, False),
            ("_location", "_location",fhirprimitive.FHIRPrimitive, False, None, False),
            ("outcome", "outcome", resource.Resource, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class BundleEntrySearch(backboneelement.BackboneElement):
    """ Search related information.
    
    Information about the search process that lead to the creation of this
    entry.
    """
    
    resource_type = "BundleEntrySearch"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        
        """ match | include | outcome - why this is in the result set.
        Type `str`. """
        
        self._mode = None
        
        """ extension for fhir primitive  mode"""
        
        self.score = None
        
        """ Search ranking (between 0 and 1).
        Type `float`. """
        
        self._score = None
        
        """ extension for fhir primitive  score"""
        
        super(BundleEntrySearch, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleEntrySearch, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, False),
            ("_mode", "_mode",fhirprimitive.FHIRPrimitive, False, None, False),
            ("score", "score", float, False, None, False),
            ("_score", "_score",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


class BundleLink(backboneelement.BackboneElement):
    """ Links related to this Bundle.
    
    A series of links that provide context to this bundle.
    """
    
    resource_type = "BundleLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.relation = None
        
        """ See http://www.iana.org/assignments/link-relations/link-
        relations.xhtml#link-relations-1.
        Type `str`. """
        
        self._relation = None
        
        """ extension for fhir primitive  relation"""
        
        self.url = None
        
        """ Reference details for the link.
        Type `str`. """
        
        self._url = None
        
        """ extension for fhir primitive  url"""
        
        super(BundleLink, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BundleLink, self).elementProperties()
        js.extend([
            ("relation", "relation", str, False, None, True),
            ("_relation", "_relation",fhirprimitive.FHIRPrimitive, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import fhirdate
from . import identifier
from . import signature
from . import fhirprimitive

