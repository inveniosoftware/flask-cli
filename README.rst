===========
 Flask-CLI
===========

About
=====

Flask-CLI is a backport of Flask 1.0 new click integration to Flask 0.10. Do not install this package if you use Flask 1.0+.

Installation
============

Flask-CLI is on PyPI so all you need is: ::

    pip install flask-cli


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

Documentation
=============

Documentation is readable at http://flask-cli.readthedocs.org or can be
build using Sphinx: ::

    pip install Sphinx
    python setup.py build_sphinx

Testing
=======

Running the test suite is as simple as: ::

    python setup.py test
