"""flake8_strings tests."""

from __future__ import unicode_literals

import ast
import unittest

from flake8_strings import StringQuotes, StringChecker


def line_is_valid(physical_line, string_quotes):
    """Validates the string and bytes nodes in a line have correct string quotes.

    Args:
        physical_line (str):
        string_quotes (str):

    Returns:
        bool: Whether the node's in the line have valid string quotes.
    """
    module = ast.parse(physical_line)
    for node in ast.walk(module):
        if isinstance(node, ast.Str) or isinstance(node, ast.Bytes):
            return StringChecker.string_quotes_are_valid(node,
                                                         string_quotes,
                                                         physical_line)


class StringQuotesTestCase(unittest.TestCase):
    def test_double_string(self):
        line = 's = "Hello"'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_string(self):
        line = "s = 'Hello'"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_single_double_quote_escape(self):
        line = 's = \'He said, "Hello."\''
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_double_single_quote_escape(self):
        line = 's = "Joe\'s answer."'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_double_empty_string(self):
        line = 's = ""'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_empty_string(self):
        line = "s = ''"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_empty_docstring(self):
        line = 's = """"""'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_empty_triple_quoted(self):
        line = "s = ''''''"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_docstring(self):
        line = 's = """Hello"""'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_triple_quoted_string(self):
        line = "s = '''Hello'''"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_double_raw_string(self):
        line = 's = r"Hello"'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_raw_string(self):
        line = "s = r'Hello'"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_double_capital_raw_string(self):
        line = 's = R"Hello"'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_capital_raw_string(self):
        line = "s = R'Hello'"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_double_bytes(self):
        line = 's = b"Hello"'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_bytes(self):
        line = "s = b'Hello'"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_double_capital_bytes(self):
        line = 's = B"Hello"'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_capital_bytes(self):
        line = "s = B'Hello'"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_double_unicode(self):
        line = 's = u"Hello"'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_unicode(self):
        line = "s = u'Hello'"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_double_capital_unicode(self):
        line = 's = U"Hello"'
        self.assertFalse(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_single_capital_unicode(self):
        line = "s = U'Hello'"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertFalse(line_is_valid(line, StringQuotes.double))

    def test_raw_doc_string(self):
        line = 's = r"""Hello"""'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_raw_triple_quoted_string(self):
        line = 's = r"""Hello"""'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_multi_line_doc_string(self):
        line = 's = """Hello\n"""'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_triple_quoted_multi_line_string(self):
        line = "s = '''Hello\n'''"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_empty_multi_line_doc_string(self):
        line = 's = """\n"""'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_empty_triple_quoted_multi_line_string(self):
        line = "s = '''\n'''"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_ignore_double_noqa(self):
        line = 'ignore_double_string = "Hello"  # noqa'
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))

    def test_ignore_single_noqa(self):
        line = "ignore_double_string = 'Hello'  # noqa"
        self.assertTrue(line_is_valid(line, StringQuotes.single))
        self.assertTrue(line_is_valid(line, StringQuotes.double))


class StringCheckerTestCase(unittest.TestCase):
    def setUp(self):
        file_name = 'tests/S800.py'
        tree = ast.parse(open(file_name, mode='rt').read())
        self.checker = StringChecker(tree, file_name)

    def test_single(self):
        self.checker.string_quote = StringQuotes.single
        errors = []
        for error in self.checker.run():
            errors.append(error[:2])

        self.assertEqual(
            errors,
            [(1, 9), (7, 15), (16, 13), (19, 21), (22, 14), (25, 22), (28, 17), (31, 25)])

    def test_double(self):
        self.checker.string_quote = StringQuotes.double
        errors = []
        for error in self.checker.run():
            errors.append(error[:2])

        self.assertEqual(
            errors,
            [(2, 9), (8, 15), (17, 13), (20, 21), (23, 14), (26, 22), (29, 17), (32, 25)])

if __name__ == '__main__':
    unittest.main()
