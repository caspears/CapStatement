#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#  2018, SMART Health IT.


from . import element


class ExtensionElement(element.Element):
    """ An element with extensions and modifierExtensions.
    
    A resource that includes narrative, extensions, and contained resources.
    """
    
    resource_type = "DomainResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.extension = None
        """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.modifierExtension = None
        """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """
                
        super(ExtensionElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExtensionElement, self).elementProperties()
        js.extend([
            ("extension", "extension", extension.Extension, True, None, False),
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False)
        ])
        return js


import sys
try:
    from . import extension
except ImportError:
    extension = sys.modules[__package__ + '.extension']
