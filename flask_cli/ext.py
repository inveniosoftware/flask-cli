# -*- coding: utf-8 -*-
#
# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Flask extension to enable CLI."""

from . import AppGroup


class FlaskCLI(object):

    """Flask-CLI extension.

    Initialization of the extension:

    >>> from flask import Flask
    >>> from flask_cli import FlaskCLI
    >>> app = Flask('myapp')
    >>> FlaskCLI(app)

    or alternatively using the factory pattern:

    >>> app = Flask('myapp')
    >>> ext = FlaskCLI()
    >>> ext.init_app(app)
    """

    def __init__(self, app=None):
        """Initialize the Flask-CLI."""
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize a Flask application."""
        # Follow the Flask guidelines on usage of app.extensions
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        if 'flask-cli' in app.extensions:
            raise RuntimeError("Flask-CLI application already initialized")
        app.extensions['flask-cli'] = self

        if not hasattr(app, 'cli'):
            app.cli = AppGroup(app)
