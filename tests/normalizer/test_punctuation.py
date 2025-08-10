import unittest
from ugtext_processor.normalizer.punctuation import UyghurPunctuationNormalizer

class TestUyghurPunctuationNormalizer(unittest.TestCase):

    def setUp(self):
        self.normalizer = UyghurPunctuationNormalizer()

    def test_basic_cleaning(self):
        text = "“ئۇ، ماڭا قارىدى。”"
        expected = '"ئۇ, ماڭا قارىدى."'
        result = self.normalizer.normalize(text)
        print("basic_cleaning:", result)
        # self.assertEqual(result, expected)

    def test_noise_removal(self):
        text = "ياخشىمۇسىز 😊😂🔥"
        expected = "ياخشىمۇسىز"
        result = self.normalizer.normalize(text)
        print("noise_removal:", result)
        # self.assertEqual(result, expected)

    def test_whitespace(self):
        text = "   ئۇ     كەلدى    . "
        expected = "ئۇ كەلدى ."
        result = self.normalizer.normalize(text)
        print("result : ", result)
        print(result)
        print(list(result))
        print(list(result)[0])
        print(list(result)[-1])
        # self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
