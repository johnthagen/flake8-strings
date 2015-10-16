PEP-8 String Quote Consistency
==============================

.. image:: https://badge.fury.io/py/flake8-strings.png
    :target: http://badge.fury.io/py/flake8-strings

Check the PEP-8 string quote consistency.  This plugin does not validate docstring formats.
See the ``pep257`` package for that.

This module provides a plugin for ``flake8``, the Python code checker.

Installation
------------

You can install, upgrade, uninstall ``flake8-strings`` with these commands::

  $ pip install flake8-strings
  $ pip install --upgrade flake8-strings
  $ pip uninstall flake8-strings


Plugin for Flake8
-----------------

When both ``flake8`` and ``flake8-strings`` are installed, the plugin is
available in ``flake8``::

  $ flake8 --version
  2.0 (pep8: 1.4.3, pyflakes: 0.6.1, flake8-strings: 0.1)

By default the plugin is enabled and set enforce single quoted strings (e.g. ``'Hello'``).


0.1 - 2013-02-11
````````````````
* First release.