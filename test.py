"""Define tests for jinja2-python-version."""

import platform
import unittest

from jinja2 import Environment


class TestPackagePath(unittest.TestCase):
    """Define test case for extension importing paths."""

    def test_package_path(self):
        """Test PythonVersionExtensions can be loaded at package level."""
        try:
            Environment(extensions=['jinja2_python_version.PythonVersionExtension'])
        except AttributeError:
            self.fail("AttributeError raised unexpectedly.")


class TestGlobalIsLoaded(unittest.TestCase):
    """Define test case for template global variable."""

    def setUp(self):
        """Set up test case."""
        self.environment = Environment(extensions=['jinja2_python_version.PythonVersionExtension'])

    def test_global_is_set(self):
        """Test global variable is loaded."""
        self.assertIn('python_version', self.environment.globals)


class TestVersionOutput(unittest.TestCase):
    """Define test case for version output."""

    def setUp(self):
        """Set up test case."""
        self.environment = Environment(extensions=['jinja2_python_version.PythonVersionExtension'])
        self.version = [str(x) for x in platform.python_version_tuple()]

    def test_micro_versions(self):
        """Test micro version output."""
        template = self.environment.from_string('{{ python_version.micro }}')
        output = template.render()
        minor_version = '.'.join(self.version[:3])
        self.assertEqual(minor_version, output)

    def test_minor_versions(self):
        """Test minor version output."""
        template = self.environment.from_string('{{ python_version.minor }}')
        output = template.render()
        minor_version = '.'.join(self.version[:2])
        self.assertEqual(minor_version, output)

    def test_major_versions(self):
        """Test major version output."""
        template = self.environment.from_string('{{ python_version.major }}')
        output = template.render()
        minor_version = '.'.join(self.version[:1])
        self.assertEqual(minor_version, output)

    def test_versions(self):
        """Test version output."""
        template = self.environment.from_string('{{ python_version }}')
        output = template.render()
        minor_version = '.'.join(self.version[:2])
        self.assertEqual(minor_version, output)


if __name__ == '__main__':
    unittest.main()
