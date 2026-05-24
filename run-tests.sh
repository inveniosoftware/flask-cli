#!/bin/sh
# SPDX-FileCopyrightText: 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

pydocstyle flask_cli/__init__.py flask_cli/ext.py flask_cli/version.py \
  flask_cli/version.py tests/*.py && \
# isort -rc -c -df **/*.py && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test && \
sphinx-build -qnNW -b doctest docs docs/_build/doctest
