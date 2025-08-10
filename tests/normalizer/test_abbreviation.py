import unittest
from ugtext_processer.normalizer.abbreviation import UyghurAbbreviation

class TestUyghurAbbreviation(unittest.TestCase):

    def setUp(self):
        self.normalizer = UyghurAbbreviation()

    def test_abbreviation_conversion(self):
        test_cases = [
            ("kg بۇ بىرلىككە قاراڭ", "بۇ بىرلىككە قاراڭ كىلوگىرام"),
            ("cm kg بۇ بىرلىككە قاراڭ", "بۇ بىرلىككە قاراڭ سېنتىمىتىر كىلوگىرام"),
            ("بۇ بىرلىككە قاراڭ KG", "بۇ بىرلىككە قاراڭ كىلوگىرام"),
            ("بۇ بىرلىككە قاراڭ Cm", "بۇ بىرلىككە قاراڭ سېنتىمىتىر"),
            ("kg cm kg cm", "سېنتىمىتىر كىلوگىرام"),
            ("ئۇ 5kg ئېلىپ كەلدى", "ئۇ 5kg ئېلىپ كەلدى"),
        ]

        for text, expected in test_cases:
            with self.subTest(text=text):
                result = self.normalizer.convert(text)
                print("text : ",text)
                print("result : ",result)

if __name__ == '__main__':
    unittest.main()