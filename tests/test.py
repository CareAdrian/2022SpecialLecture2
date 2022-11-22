import unittest
from tests.ss2022 import CSVPrinter 

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("tests/sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
