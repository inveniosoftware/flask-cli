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

Use this library as fallback when importing from ``flask.cli``.

.. code-block:: python

   try:
       from flask.cli import FlaskGroup
   except ImportError
       from flask_cli.cli import FlaskGroup

Note Flask-CLI is only a backport of ``flask.cli``. Most noteably, there's no integration into the Flask application object. E.g. the following won't work:

.. code-block:: python

    app = Flask(__name__)

    @app.cli.command()
    def initdb():
        """Initialize the database."""
        print 'Init the db'

.. include:: ../CHANGES

.. include:: ../CONTRIBUTING.rst

License
=======

.. include:: ../LICENSE

.. include:: ../AUTHORS
