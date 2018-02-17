"""Include Python version in Jinja2 templates."""

import platform

from jinja2.ext import Extension


class PythonVersion():
    """An object that contains python version information."""

    _version = platform.python_version_tuple()
    major = '{}'.format(_version[0])
    minor = '{}.{}'.format(_version[0], _version[1])
    micro = '{}.{}.{}'.format(_version[0], _version[1], _version[2])

    def __str__(self):
        """Return Python version up to minor."""
        return self.minor


class PythonVersionExtension(Extension):
    """Jinja extension that adds Python versions globals."""

    def __init__(self, environment):
        """Extend environment by adding globals."""
        super().__init__(environment)

        environment.globals['python_version'] = PythonVersion()
