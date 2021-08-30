#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import json
import codecs
import logging

logger = __import__('logging').getLogger(__name__)


class Recipe(object):

    def __init__(self, buildout, name, options,):
        self.name = name
        self.filename = options['output-file']
        self.hosts = ""
        self.redirect = ""
        if 'hosts-text' in options:
            self.hosts = options['hosts-text']
            print(self.hosts)
        elif 'hosts-file' in options:
            self.hostsFile = open(options['hosts-file'], "r+")
        if 'redirect' in options:
            self.redirect = options['redirect']
            print(self.redirect)
            print("TESTING")

    def install(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for line in self.hostsFile.readlines():
                f.write(line.rstrip('\n') + '\t' + self.redirect + '\n' )
        return self.filename

    def update(self):
        return self.install()
