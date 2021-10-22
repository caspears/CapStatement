#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 on 2018-12-20.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import coverageeligibilityresponse
from .fhirdate import FHIRDate


class CoverageEligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        return coverageeligibilityresponse.CoverageEligibilityResponse(js)
    
    def testCoverageEligibilityResponse1(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse1(inst2)
    
    def implCoverageEligibilityResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")

