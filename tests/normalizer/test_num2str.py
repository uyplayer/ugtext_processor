import sys
import os
import unittest

from ugtext_processer.normalizer.num2str import UyghurNumberConverter

class TestUyghurNumberConverter(unittest.TestCase):

    def setUp(self):
        self.converter = UyghurNumberConverter()

    def test_single_digit(self):
        result = self.converter.num2str(5.1)
        print("5 →", result)
        self.assertEqual(result, "بەش")

    def test_two_digits(self):
        result = self.converter.num2str(21)
        print("21 →", result)
        self.assertEqual(result, "يىگىرمە بىر")

    def test_three_digits(self):
        result = self.converter.num2str(305)
        print("305 →", result)
        self.assertEqual(result, "ئۈچ يۈز بەش")

    def test_large_integer(self):
        result = self.converter.num2str(1234567)
        print("1234567 →", result)
        self.assertIn("مىليون", result)

    def test_negative_number(self):
        result = self.converter.num2str(-12)
        print("-12 →", result)
        self.assertTrue(result.startswith("مىنۇس"))

    def test_decimal_number(self):
        result = self.converter.num2str(12.5)
        print("12.5 →", result)
        self.assertIn("پۈتۈن", result)
        self.assertIn("ئوندا", result)

    def test_zero(self):
        result = self.converter.num2str(0)
        print("0 →", result)
        self.assertEqual(result, "نۆل")

    def test_truncate_long_decimal(self):
        long_decimal = 0.123456789123456789
        result = self.converter.num2str(long_decimal)
        print("0.123456789123456789 →", result)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
