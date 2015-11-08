================
 Flask-CLI
================
.. currentmodule:: flask_cli

.. raw:: html

    <p style="height:22px; margin:0 0 0 2em; float:right">
        <a href="https://travis-ci.org/inveniosoftware/flask-cli">
            <img src="https://travis-ci.org/inveniosoftware/flask-cli.svg?branch=master"
                 alt="travis-ci badge"/>
        </a>
        <a href="https://coveralls.io/r/inveniosoftware/flask-cli">
            <img src="https://coveralls.io/repos/inveniosoftware/flask-cli/badge.svg?branch=master"
                 alt="coveralls.io badge"/>
        </a>
    </p>


.. automodule:: flask_cli

Installation
============

The Flask-CLI package is on PyPI so all you need is:

.. code-block:: console

    $ pip install flask-cli

Usage
=====

Initialize the extension like this:

.. code-block:: python

   import click
   from flask import Flask
   from flask_cli import FlaskCLI
   app = Flask('myapp')
   FlaskCLI(app)

   @app.cli.command()
   def mycmd():
       click.echo("Test")

Import from this library instead of ``flask.cli``, e.g.:

.. code-block:: python

   from flask_cli import FlaskGroup

.. include:: ../CHANGES

.. include:: ../CONTRIBUTING.rst

License
=======

.. include:: ../LICENSE

.. include:: ../AUTHORS
