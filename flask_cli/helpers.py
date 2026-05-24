# SPDX-FileCopyrightText: 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

import os

try:
    from flask.helpers import get_debug_flag
except ImportError:

    def get_debug_flag(default=None):
        val = os.environ.get('FLASK_DEBUG')
        if not val:
            return default
        return val not in ('0', 'false', 'no')
