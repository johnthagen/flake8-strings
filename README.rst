PEP-8 String Quote Consistency
==============================

.. image:: https://travis-ci.org/johnthagen/flake8-strings.svg
    :target: https://travis-ci.org/johnthagen/flake8-strings

.. image:: https://codecov.io/github/johnthagen/flake8-strings/coverage.svg
    :target: https://codecov.io/github/johnthagen/flake8-strings

.. image:: https://img.shields.io/pypi/v/flake8-strings.svg
    :target: https://pypi.python.org/pypi/flake8-strings

.. image:: https://img.shields.io/pypi/pyversions/flake8-strings.svg
    :target: https://pypi.python.org/pypi/flake8-strings/

.. image:: https://img.shields.io/pypi/dd/flake8-strings.svg
    :target: https://pypi.python.org/pypi/flake8-strings/

*Note: Because* `flake8-quotes <https://pypi.python.org/pypi/flake8-quotes>`_ *has since
been updated and supports all of the features of this package, this package was not
uploaded to PyPI as it would have been redundant.*

This module provides a plugin for `flake8 <https://pypi.python.org/pypi/flake8>`_, the Python
code checker, that checks for
`PEP-8 string quote consistency <https://www.python.org/dev/peps/pep-0008/#string-quotes>`_.
This plugin does not validate docstring formats.
See the `pep257 <https://pypi.python.org/pypi/pep257>`_ package for that.


Installation
------------

You can install, upgrade, and uninstall ``flake8-strings`` with these commands::

    $ pip install flake8-strings
    $ pip install --upgrade flake8-strings
    $ pip uninstall flake8-strings


Plugin for Flake8
-----------------

When both ``flake8`` and ``flake8-strings`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    2.4.1 (pep8: 1.5.7, flake8-strings: 0.1, pyflakes: 0.8.1, mccabe: 0.3.1)


Run
---

By default the plugin is enabled and set to enforce single quoted
strings (as `repr() <https://docs.python.org/3/library/functions.html#repr>`_ uses)::

    $ flake8 test.py
    test.py:1:10: S800 Inconsistent string quotes found, should be '

But can be reconfigured to enforce double quoted strings::

    $ flake8 --string-quotes=double test.py
    test.py:2:10: S800 Inconsistent string quotes found, should be "

0.1 - 2015-10-17
````````````````
* First release.