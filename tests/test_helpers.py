import unittest
import happyr


class TestHelpers(unittest.TestCase):
    def test_which_r(self):
        self.assertFalse(happyr.helpers.which_r(path="/tmp/", status=1, exit_on_error=False))
        
    def test_set_lib(self):
        self.assertEqual(".libPaths()", happyr.helpers.set_lib(None))
        self.assertEqual("'/tmp'", happyr.helpers.set_lib("/tmp"))

    def test_set_cran(self):
        self.assertEqual("getOption('repos')", happyr.helpers.set_cran(None))
        self.assertEqual(
            "'https://cloud.r-project.org'", happyr.helpers.set_cran("https://cloud.r-project.org")
        )


if __name__ == "__main__":
    unittest.main()
