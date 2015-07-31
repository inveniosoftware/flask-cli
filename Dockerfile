# This file is part of Flask-CLI
# Copyright (C) 2015 CERN.
#
# Flask-CLI is free software; you can redistribute it and/or modify it under
# the terms of the Revised BSD License; see LICENSE file for more details.

# Use Python-2.7:
FROM python:2.7

# Install some prerequisites ahead of `setup.py` in order to profit
# from the docker build cache:
RUN pip install coveralls \
                ipython \
                pep257 \
                pytest \
                pytest-cache \
                pytest-cov \
                Sphinx

# Add sources to `code` and work there:
WORKDIR /code
ADD . /code

# Install flask-cli:
RUN pip install -e .

# Run container as user `flask-cli` with UID `1000`, which should match
# current host user in most situations:
RUN adduser --uid 1000 --disabled-password --gecos '' flaskcli && \
    chown -R flaskcli:flaskcli /code

# Run test suite instead of starting the application:
USER flaskcli
CMD ["python", "setup.py", "test"]
