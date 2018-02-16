=====================
Jinja2 Python Version
=====================

A Jinja extenstion that creates a global variable with Python version
information for your Jinja2 templates:

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

    # ('3', '6', '4')
    template = env.from_string("{{ python_version.tuple }}")

    template.render()
