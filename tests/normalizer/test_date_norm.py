import unittest
from ugtext_processer.normalizer.date_norm import UyghurDateNormalizer

class TestUyghurDateNormalizer(unittest.TestCase):

    def setUp(self):
        self.normalizer = UyghurDateNormalizer()

    def test_find_dates(self):
        text = " 2025-07-14  14/07/2025"
        found = self.normalizer.find_dates(text)
        print(found)

    def test_find_times(self):
        text = "Start at 08:30 or 15:45:22."
        expected = ['08:30', '15:45:22']
        found = self.normalizer.find_times(text)
        print(found)

    def test_normalize_date_only(self):
        text = "تارىخ 2025/07/14."
        result = self.normalizer.normalize_all(text)
        print(result)

    def test_normalize_time_only(self):
        text = "ۋاقىت 08:30 ۋە 14:00:05."
        result = self.normalizer.normalize_all(text)
        print(result)

    def test_full_normalization(self):
        text = " 2025-07-14  08:00  15:45:22."
        result = self.normalizer.normalize_all(text)
        print(result)

if __name__ == '__main__':
    unittest.main()
