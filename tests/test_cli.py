import unittest
import happyr


class TestCliArgParser(unittest.TestCase):
    def test_parser_help(self):
        with self.assertRaises(SystemExit):
            parser = happyr.cli.arg_parser(["-h"])

    def test_style_help(self):
        with self.assertRaises(SystemExit):
            parser = happyr.cli.arg_parser(["style", "-h"])

    def test_lint_help(self):
        with self.assertRaises(SystemExit):
            parser = happyr.cli.arg_parser(["lint", "-h"])


if __name__ == "__main__":
    unittest.main()
