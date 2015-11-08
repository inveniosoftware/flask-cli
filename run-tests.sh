#!/bin/sh
#
# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-CLI is free software; you can redistribute it and/or modify it under
# the terms of the Revised BSD License; see LICENSE file for more details.

pep257 flask_cli/__init__.py flask_cli/ext.py flask_cli/version.py \
  flask_cli/version.py tests/*.py && \
# isort -rc -c -df **/*.py && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test && \
sphinx-build -qnNW -b doctest docs docs/_build/doctest
