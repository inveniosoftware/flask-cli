# SPDX-FileCopyrightText: 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Flask applications fixture."""

from __future__ import absolute_import, print_function

from flask import Flask

app1 = Flask('app1')
app2 = Flask('app2')
