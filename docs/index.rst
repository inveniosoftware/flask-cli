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

CLI Plugins
-----------

Flask extensions can always patch the `Flask.cli` instance with more
commands if they want.  However there is a second way to add CLI plugins
to Flask which is through `setuptools`.  If you make a Python package that
should export a Flask command line plugin you can ship a `setup.py` file
that declares an entrypoint that points to a click command:

Example `setup.py`::

    from setuptools import setup

    setup(
        name='flask-my-extension',
        ...
        entry_points='''
            [flask.commands]
            my-command=mypackage.commands:cli
        ''',
    )

Inside `mypackage/comamnds.py` you can then export a Click object::

    import click

    @click.command()
    def cli():
        """This is an example command."""

Once that package is installed in the same virtualenv as Flask itself you
can run ``flask my-command`` to invoke your command.  This is useful to
provide extra functionality that Flask itself cannot ship.

Import from this library instead of ``flask.cli``, e.g.:

.. code-block:: python

   from flask_cli import FlaskGroup

.. include:: ../CHANGES

.. include:: ../CONTRIBUTING.rst

License
=======

.. include:: ../LICENSE

.. include:: ../AUTHORS
