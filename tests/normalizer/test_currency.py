import unittest
from ugtext_processor.normalizer.currency import UyghurCurrency

class TestUyghurCurrency(unittest.TestCase):

    def setUp(self):
        self.converter = UyghurCurrency()

    def test_currency_conversion(self):
        test_cases = [
            ("$100", "100 ئامېرىكا دوللىرى"),
            ("€250", "250 ياۋرو"),
            ("¥300", "300 يۈەن"),
            ("₺75", "75 تۈركىيە لىراسى"),
            ("USD400", "400 ئامېرىكا دوللىرى"),
            ("EUR200", "200 ياۋرو"),
            ("ئۇ $50 ۋە EUR100 بىلەن سېتىۋالدى", "ئۇ 50 ئامېرىكا دوللىرى ۋە 100 ياۋرو بىلەن سېتىۋالدى"),
            ("$123.45 ۋە ¥88.88", "123.45 ئامېرىكا دوللىرى ۋە 88.88 يۈەن"),
            ("TRY900 JPY1000", "900 تۈركىيە لىراسى 1000 ياپونىيە يېنى"),
        ]

        for text, expected in test_cases:
            with self.subTest(text=text):
                result = self.converter.convert_currency_symbol_to_text(text)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()