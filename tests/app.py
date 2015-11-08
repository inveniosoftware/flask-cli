# -*- coding: utf-8 -*-
#
# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Flask application fixture."""

from __future__ import absolute_import, print_function

from flask import Flask

testapp = Flask('testapp')
