#!/usr/bin/env python
import codecs
from setuptools import setup
from setuptools import find_packages

entry_points = {
    'zc.buildout': [
        'json = nti.recipes.haproxy:Recipe',
        'default = nti.recipes.haproxy:Recipe',
    ]
}

TESTS_REQUIRE = [
    'pyhamcrest',
    'zope.testrunner',
]


def _read(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()


setup(
    name='nti.recipes.haproxy',
    version='1.0.1.dev0',
    author='Zach Arani',
    author_email='zach.arani@nextthought.com',
    description="zc.buildout recipe that programatically creates Haproxy map files",
    long_description=(
        _read('README.rst')
        + '\n\n'
        + _read("CHANGES.rst")
    ),
    license='Apache',
    keywords='buildout haproxy',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Buildout',
        'License :: OSI Approved :: Apache Software License',
    ],
    url="https://github.com/OpenNTI/nti.recipes.haproxy",
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['nti', 'nti.recipes'],
    tests_require=TESTS_REQUIRE,
    install_requires=[
        'setuptools',
        'zc.buildout',
        'zc.recipe.deployment',
    ],
    extras_require={
        'test': TESTS_REQUIRE,
        'docs': [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'sphinx_rtd_theme',
        ]
    },
    entry_points=entry_points,
)
