# -*- coding: utf-8 -*-
#
# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Flask-CLI is a backport of Flask 1.0 new click integration to v0.10.

Do not install this package if you use Flask 1.0+.

Full documentation of Flask's new click command line integration can be found
at: http://flask.pocoo.org/docs/dev/cli/.
"""

from __future__ import absolute_import, print_function

try:
    from flask.cli import AppGroup, DispatchingApp, FlaskGroup, \
        NoAppException, ScriptInfo, app_option, cli, debug_option, \
        find_best_app, locate_app, main, pass_script_info, \
        prepare_exec_for_file, run_command, script_info_option, \
        set_app_value, set_debug_value, shell_command, with_appcontext
except ImportError:
    from flask_cli.cli import AppGroup, DispatchingApp, FlaskGroup, \
        NoAppException, ScriptInfo, app_option, cli, debug_option, \
        find_best_app, locate_app, main, pass_script_info, \
        prepare_exec_for_file, run_command, script_info_option, \
        set_app_value, set_debug_value, shell_command, with_appcontext

from .ext import FlaskCLI
from .version import __version__

__all__ = (
    '__version__', 'FlaskCLI', 'AppGroup', 'DispatchingApp', 'FlaskGroup',
    'NoAppException', 'ScriptInfo', 'app_option', 'cli', 'debug_option',
    'find_best_app', 'locate_app', 'main', 'pass_script_info',
    'prepare_exec_for_file', 'run_command', 'script_info_option',
    'set_app_value', 'set_debug_value', 'shell_command', 'with_appcontext',
)

if __name__ == '__main__':
    main(as_module=True)
