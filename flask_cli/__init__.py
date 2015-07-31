# -*- coding: utf-8 -*-
#
# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Flask-CLI is a partial backport of Flask 1.0 new click integration to v0.10.

Do not install this package if you use Flask 1.0+.

Full documentation of Flask's new click command line integration can be found
at: http://flask.pocoo.org/docs/dev/cli/.
"""

from __future__ import absolute_import, unicode_literals, print_function

from .version import __version__

__all__ = ('__version__', )
