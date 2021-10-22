#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.6.0-bd605d07 on 2018-12-20.
#  2018, SMART Health IT.


import os
import io
import unittest
import json
from . import specimendefinition
from .fhirdate import FHIRDate


class SpecimenDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SpecimenDefinition", js["resourceType"])
        return specimendefinition.SpecimenDefinition(js)
    
    def testSpecimenDefinition1(self):
        inst = self.instantiate_from("specimendefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SpecimenDefinition instance")
        self.implSpecimenDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("SpecimenDefinition", js["resourceType"])
        inst2 = specimendefinition.SpecimenDefinition(js)
        self.implSpecimenDefinition1(inst2)
    
    def implSpecimenDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

