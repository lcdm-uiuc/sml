import unittest

import sml_auto
import sml_boston
import sml_census
import sml_chronic
import sml_computer
import sml_iris
import sml_seeds
import sml_spam
import sml_titanic
import sml_wine
import sys
import traceback

class SmlIntegrationTests(unittest.TestCase):

    # print("Testing General Model Building Functionality")
    def test_auto(self):
        assert sml_auto.test() is not None
    def test_boston(self):
        assert sml_boston.test() is not None
    def test_census(self):
        assert sml_census.test() is not None
    def test_chronic(self):
        assert sml_chronic.test() is not None
    def test_computer(self):
        assert sml_computer.test() is not None
    def test_iris(self):
        assert sml_iris.test() is not None
    def test_seeds(self):
        assert sml_seeds.test() is not None
    def test_spam(self):
        assert sml_spam.test() is not None
    def test_titanic(self):
        assert sml_titanic.test() is not None
    def test_wine(self):
        assert sml_wine.test() is not None
if __name__ == '__main__':
    unittest.main()
