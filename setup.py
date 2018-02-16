"""Setup script for jinja2_python_version."""
import os
import re

from setuptools import setup


def get_version(*file_paths):
    """Retrieve the version from given file."""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version('jinja2_python_version', '__init__.py')

readme = open('README.rst').read()

setup(
    name='jinja2-python-version',
    version=version,
    description="""A Jinja2 extenstion that adds python version to templates.""",
    long_description=readme,
    author='Federico Jaramillo Martínez',
    author_email='federicojaramillom@gmail.com',
    url='https://github.com/jmfederico/jinja2-python-version',
    packages=[
        'jinja2_python_version',
    ],
    include_package_data=True,
    install_requires=['jinja2'],
    license="BSD License",
    keywords='jinja2 extension python versions',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
