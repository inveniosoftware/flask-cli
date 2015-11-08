# -*- coding: utf-8 -*-
#
# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Tests for extension."""

from __future__ import absolute_import, print_function

import click
import pytest
from click.testing import CliRunner
from flask import Flask, current_app

from flask_cli import FlaskCLI, ScriptInfo


def test_ext_init():
    """Test of find_best_app."""
    app = Flask('exttest')
    FlaskCLI(app)
    assert isinstance(app.cli, click.Group)

    app = Flask('exttest')
    ext = FlaskCLI()
    ext.init_app(app)
    assert isinstance(app.cli, click.Group)
    assert app.shell_context_processors == []
    pytest.raises(RuntimeError, ext.init_app, app)


def test_ext_shelcontext():
    """Test creating commands."""
    app = Flask('exttest')
    cli = FlaskCLI(app)

    @app.shell_context_processor
    def myshellctx():
        return {'cli': cli}

    assert len(app.shell_context_processors) == 1
    rv = app.make_shell_context()
    assert rv['app'] == app
    assert rv['cli'] == cli
    assert 'g' in rv


def test_ext_cmd():
    """Test creating commands."""
    app = Flask('exttest')
    FlaskCLI(app)

    @app.cli.command()
    def test1():
        click.echo("TEST")

    @app.cli.command(with_appcontext=True)
    def test2():
        click.echo(current_app.name)

    obj = ScriptInfo(create_app=lambda info: app)
    runner = CliRunner()
    result = runner.invoke(test1, obj=obj)
    assert result.exit_code == 0
    assert result.output == 'TEST\n'

    obj = ScriptInfo(create_app=lambda info: app)
    runner = CliRunner()
    result = runner.invoke(test2, obj=obj)
    assert result.exit_code == 0
    assert result.output == 'exttest\n'
