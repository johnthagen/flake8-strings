"""Checker for PEP-8 String Quote Consistency.

Defaults to single-quoted strings to be consistent with repr().
"""

from __future__ import unicode_literals

import ast
import sys
from typing import Tuple  # noqa

import pep8

__version__ = '0.1'

if sys.version_info < (3, 0):
    ast.Bytes = ast.Str


class StringQuotes(object):
    single = "'"
    double = '"'
    triple_single = "'''"
    triple_double = '"""'


opposite_string_quotes = {
    StringQuotes.single: StringQuotes.double,
    StringQuotes.double: StringQuotes.single,
    StringQuotes.triple_single: StringQuotes.triple_double,
    StringQuotes.triple_double: StringQuotes.triple_single
}


class StringChecker(object):
    """PEP-8 String Quote Consistency Checker."""

    name = 'flake8-strings'
    version = __version__

    def __init__(self,
                 tree,
                 file_name  # type: str
                 ):
        # type: (...) -> StringChecker
        self.tree = tree
        self.file_name = file_name

    @classmethod
    def add_options(cls, parser):
        # type (...) -> None
        parser.add_option('--string-quotes',
                          default='single',
                          action='store',
                          type='choice',
                          choices=['single', 'double'],
                          help='String quoting style to enforce.')
        parser.config_options.append('string-quotes')

    @classmethod
    def parse_options(cls, options):
        # type (...) -> None
        if options.string_quotes == 'single':
            cls.string_quote = StringQuotes.single
        else:
            cls.string_quote = StringQuotes.double

    @staticmethod
    def string_quotes_are_valid(node,  # type: ast.AST
                                valid_string_quote,  # type: str
                                physical_line  # type: str
                                ):
        # type: (...) -> bool
        """Checks a string or bytes node's string quotes for validity.

        Args:
            node: Node to verify quotes of.
            valid_string_quote: The correct string quote that should
                be used.
            physical_line: The physical line that node originated from.

        Returns:
            Whether the node's string quotes are valid.
        """
        # Ignore multi-line strings.
        if node.col_offset == -1:
            return True

        if pep8.noqa(physical_line):
            return True

        max_prefix_len = len('r"""')
        prefix = physical_line[node.col_offset:node.col_offset+max_prefix_len]

        if isinstance(node, ast.Bytes):
            node.s = node.s.decode('ascii')

        # Ignore string prefix (e.g. r'').
        if prefix[0].isalpha():
            prefix = prefix[1:]

        string_quote = prefix[0]
        if (string_quote != valid_string_quote and
           opposite_string_quotes[string_quote] not in node.s and
           not prefix.startswith(StringQuotes.triple_single) and
           not prefix.startswith(StringQuotes.triple_double)):
            return False
        else:
            return True

    def run(self):
        # type: () -> Tuple[int, int, str, type]
        """Checks all string and bytes nodes in a file for quote consistency.

        Yields:
            Location of an error in a line.
        """
        with open(self.file_name, mode='rt') as file:
            physical_lines = file.readlines()
            for node in ast.walk(self.tree):
                if isinstance(node, ast.Str) or isinstance(node, ast.Bytes):
                    physical_line = physical_lines[node.lineno-1]

                    if not self.string_quotes_are_valid(node, self.string_quote, physical_line):
                            yield (node.lineno, node.col_offset,
                                   'S800 Inconsistent string quotes found, '
                                   'should be {}'.format(self.string_quote),
                                   type(self))
