# -*- coding: utf-8 -*-
#
# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-AppFactory is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""Tests for Flask backport."""

from __future__ import absolute_import, print_function

import click
import pytest
from click.testing import CliRunner
from flask import Flask, current_app

from flask_cli.cli import AppGroup, FlaskGroup, NoAppException, ScriptInfo, \
    find_best_app, locate_app, script_info_option, with_appcontext
from flask_cli.ext import FlaskCLI


def test_cli_name():
    """Test the name of the CLI."""
    from app import testapp
    FlaskCLI(testapp)
    assert testapp.cli.name == testapp.name


def test_find_best_app():
    """Test of find_best_app."""
    class mod:
        app = Flask('appname')
    assert find_best_app(mod) == mod.app

    class mod:
        application = Flask('appname')
    assert find_best_app(mod) == mod.application

    class mod:
        myapp = Flask('appname')
    assert find_best_app(mod) == mod.myapp

    class mod:
        myapp = Flask('appname')
        myapp2 = Flask('appname2')

    pytest.raises(NoAppException, find_best_app, mod)


def test_locate_app():
    """Test of locate_app."""
    assert locate_app("app").name == "testapp"
    assert locate_app("app:testapp").name == "testapp"
    assert locate_app("multiapp:app1").name == "app1"
    pytest.raises(RuntimeError, locate_app, "app:notanapp")


def test_scriptinfo():
    """Test of ScriptInfo."""
    obj = ScriptInfo(app_import_path="app:testapp")
    assert obj.load_app().name == "testapp"
    assert obj.load_app().name == "testapp"

    def create_app(info):
        return Flask("createapp")

    obj = ScriptInfo(create_app=create_app)
    app = obj.load_app()
    assert app.name == "createapp"
    assert obj.load_app() == app


def test_with_appcontext():
    """Test of with_appcontext."""
    @click.command()
    @with_appcontext
    def testcmd():
        click.echo(current_app.name)

    obj = ScriptInfo(create_app=lambda info: Flask("testapp"))

    runner = CliRunner()
    result = runner.invoke(testcmd, obj=obj)
    assert result.exit_code == 0
    assert result.output == 'testapp\n'


def test_appgroup():
    """Test of with_appcontext."""
    @click.group(cls=AppGroup)
    def cli():
        pass

    @cli.command(with_appcontext=True)
    def test():
        click.echo(current_app.name)

    @cli.group()
    def subgroup():
        pass

    @subgroup.command(with_appcontext=True)
    def test2():
        click.echo(current_app.name)

    obj = ScriptInfo(create_app=lambda info: Flask("testappgroup"))

    runner = CliRunner()
    result = runner.invoke(cli, ['test'], obj=obj)
    assert result.exit_code == 0
    assert result.output == 'testappgroup\n'

    result = runner.invoke(cli, ['subgroup', 'test2'], obj=obj)
    assert result.exit_code == 0
    assert result.output == 'testappgroup\n'


def test_flaskgroup():
    """Test FlaskGroup."""
    def create_app(info):
        return Flask("flaskgroup")

    @click.group(cls=FlaskGroup, create_app=create_app)
    @script_info_option('--config', script_info_key='config')
    def cli(**params):
        pass

    @cli.command()
    def test():
        click.echo(current_app.name)

    runner = CliRunner()
    result = runner.invoke(cli, ['test'])
    assert result.exit_code == 0
    assert result.output == 'flaskgroup\n'
