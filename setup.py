"""See README.md for package documentation."""

from setuptools import setup

from io import open
from os import path

here = path.abspath(path.dirname(__file__))

filename = path.join(here, 'kivy_garden', 'contextmenu', '_version.py')
locals = {}
with open(filename, "rb") as fh:
    exec(compile(fh.read(), filename, 'exec'), globals(), locals)
__version__ = locals['__version__']

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

URL = 'https://github.com/kivy-garden/contextmenu'

setup(
    name='kivy_garden.contextmenu',
    version=__version__,
    description='Context and application menus for Kivy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    author='Kivy',
    author_email='kivy@kivy.org',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Kivy kivy-garden',

    packages=['kivy_garden.contextmenu'],
    install_requires=[],
    extras_require={
        'dev': ['pytest>=3.6', 'wheel', 'pytest-cov', 'pycodestyle'],
        'travis': ['coveralls'],
    },
    package_data={'kivy_garden.contextmenu': ['*.kv']},
    data_files=[],
    entry_points={},
    project_urls={
        'Bug Reports': URL + '/issues',
        'Source': URL,
    },
)
