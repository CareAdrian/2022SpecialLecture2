import unittest
from ss2022.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv");
        l = printer.read()
        self.asserEqual(2, len(l))
