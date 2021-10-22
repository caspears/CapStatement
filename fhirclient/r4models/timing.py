#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 (http://hl7.org/fhir/StructureDefinition/Timing) on 2018-12-20.
#  2018, SMART Health IT.


from . import backboneelement

class Timing(backboneelement.BackboneElement):
    """ A timing schedule that specifies an event that may occur multiple times.
    
    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """
    
    resource_type = "Timing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        
        """ BID | TID | QID | AM | PM | QD | QOD | +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.event = None
        
        """ When the event occurs.
        List of `FHIRDate` items (represented as `str` in JSON). """
        
        self.repeat = None
        
        """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """
        
        super(Timing, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("event", "event", fhirdate.FHIRDate, True, None, False),
            ("repeat", "repeat", TimingRepeat, False, None, False),
        ])
        return js


from . import element

class TimingRepeat(element.Element):
    """ When the event is to occur.
    
    A set of rules that describe when the event is scheduled.
    """
    
    resource_type = "TimingRepeat"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.boundsDuration = None
        
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.boundsPeriod = None
        
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Period` (represented as `dict` in JSON). """
        
        self.boundsRange = None
        
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Range` (represented as `dict` in JSON). """
        
        self.count = None
        
        """ Number of times to repeat.
        Type `int`. """
        
        self._count = None
        
        """ extension for fhir primitive  count"""
        
        self.countMax = None
        
        """ Maximum number of times to repeat.
        Type `int`. """
        
        self._countMax = None
        
        """ extension for fhir primitive  countMax"""
        
        self.dayOfWeek = None
        
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        self._dayOfWeek = None
        
        """ extension for fhir primitive  dayOfWeek"""
        
        self.duration = None
        
        """ How long when it happens.
        Type `float`. """
        
        self._duration = None
        
        """ extension for fhir primitive  duration"""
        
        self.durationMax = None
        
        """ How long when it happens (Max).
        Type `float`. """
        
        self._durationMax = None
        
        """ extension for fhir primitive  durationMax"""
        
        self.durationUnit = None
        
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self._durationUnit = None
        
        """ extension for fhir primitive  durationUnit"""
        
        self.frequency = None
        
        """ Event occurs frequency times per period.
        Type `int`. """
        
        self._frequency = None
        
        """ extension for fhir primitive  frequency"""
        
        self.frequencyMax = None
        
        """ Event occurs up to frequencyMax times per period.
        Type `int`. """
        
        self._frequencyMax = None
        
        """ extension for fhir primitive  frequencyMax"""
        
        self.offset = None
        
        """ Minutes from event (before or after).
        Type `int`. """
        
        self._offset = None
        
        """ extension for fhir primitive  offset"""
        
        self.period = None
        
        """ Event occurs frequency times per period.
        Type `float`. """
        
        self._period = None
        
        """ extension for fhir primitive  period"""
        
        self.periodMax = None
        
        """ Upper limit of period (3-4 hours).
        Type `float`. """
        
        self._periodMax = None
        
        """ extension for fhir primitive  periodMax"""
        
        self.periodUnit = None
        
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self._periodUnit = None
        
        """ extension for fhir primitive  periodUnit"""
        
        self.timeOfDay = None
        
        """ Time of day for action.
        List of `FHIRDate` items (represented as `str` in JSON). """
        
        self.when = None
        
        """ Code for time period of occurrence.
        List of `str` items. """
        
        self._when = None
        
        """ extension for fhir primitive  when"""
        
        super(TimingRepeat, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("boundsDuration", "boundsDuration", duration.Duration, False, "bounds", False),
            ("boundsPeriod", "boundsPeriod", period.Period, False, "bounds", False),
            ("boundsRange", "boundsRange", range.Range, False, "bounds", False),
            ("count", "count", int, False, None, False),
            ("_count", "_count",fhirprimitive.FHIRPrimitive, False, None, False),
            ("countMax", "countMax", int, False, None, False),
            ("_countMax", "_countMax",fhirprimitive.FHIRPrimitive, False, None, False),
            ("dayOfWeek", "dayOfWeek", str, True, None, False),
            ("_dayOfWeek", "_dayOfWeek",fhirprimitive.FHIRPrimitive, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("_duration", "_duration",fhirprimitive.FHIRPrimitive, False, None, False),
            ("durationMax", "durationMax", float, False, None, False),
            ("_durationMax", "_durationMax",fhirprimitive.FHIRPrimitive, False, None, False),
            ("durationUnit", "durationUnit", str, False, None, False),
            ("_durationUnit", "_durationUnit",fhirprimitive.FHIRPrimitive, False, None, False),
            ("frequency", "frequency", int, False, None, False),
            ("_frequency", "_frequency",fhirprimitive.FHIRPrimitive, False, None, False),
            ("frequencyMax", "frequencyMax", int, False, None, False),
            ("_frequencyMax", "_frequencyMax",fhirprimitive.FHIRPrimitive, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("_offset", "_offset",fhirprimitive.FHIRPrimitive, False, None, False),
            ("period", "period", float, False, None, False),
            ("_period", "_period",fhirprimitive.FHIRPrimitive, False, None, False),
            ("periodMax", "periodMax", float, False, None, False),
            ("_periodMax", "_periodMax",fhirprimitive.FHIRPrimitive, False, None, False),
            ("periodUnit", "periodUnit", str, False, None, False),
            ("_periodUnit", "_periodUnit",fhirprimitive.FHIRPrimitive, False, None, False),
            ("timeOfDay", "timeOfDay", fhirdate.FHIRDate, True, None, False),
            ("when", "when", str, True, None, False),
            ("_when", "_when",fhirprimitive.FHIRPrimitive, False, None, False),
        ])
        return js


from . import codeableconcept
from . import duration
from . import fhirdate
from . import period
from . import range
from . import fhirprimitive

