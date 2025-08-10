import sys
import os
import unittest

from ugtext_processor.normalizer.num_norm import UyghurNumberNormalizer


class TestUyghurNumNorm(unittest.TestCase):

    def setUp(self):
        self.num_norm = UyghurNumberNormalizer()

    def test_norm(self):
        text = "بۈگۈن 2024/07/26، سائەت 14:30، باھاسى ¥120.5، تېمپېراتۇرا -5.0°C"
        result = self.num_norm.normalize_numbers(text)
        print(result)