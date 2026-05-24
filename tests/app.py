# SPDX-FileCopyrightText: 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Flask application fixture."""

from __future__ import absolute_import, print_function

from flask import Flask

testapp = Flask('testapp')
