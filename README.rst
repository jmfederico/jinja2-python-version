==================
🔔 PROJECT STATUS 🔔
==================
Life has taken me to now work in GO_, and do not have the time to actively maintain this project.

.. _GO: https://go.dev/

Which means this project is looking for new maintainer, please `open an issue and postulate yourself`_ if interested.


.. _`open an issue and postulate yourself`: https://github.com/jmfederico/jinja2-python-version/issues/new


=====================
Jinja2 Python Version
=====================

.. image:: https://badge.fury.io/py/jinja2-python-version.svg
    :target: https://badge.fury.io/py/jinja2-python-version

.. image:: https://github.com/jmfederico/jinja2-python-version/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/jmfederico/jinja2-python-version/actions/workflows/tests.yml

A Jinja extension that creates a global variable with Python version
information for your Jinja2 templates:

Compatible with Jinja2 versions 2.x and 3.x.

Usage
-----
.. code-block:: console

    $ pip install jinja2-python-version

.. code-block:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_python_version.PythonVersionExtension'])

    # 3.6
    template = env.from_string("{{ python_version }}")

    # 3.6
    template = env.from_string("{{ python_version.minor }}")

    # 3
    template = env.from_string("{{ python_version.major }}")

    # 3.6.4
    template = env.from_string("{{ python_version.micro }}")

    template.render()
