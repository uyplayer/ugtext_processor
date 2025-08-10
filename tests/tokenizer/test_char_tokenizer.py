from unittest import TestCase

from ugtext_processer.tokenizer.char_tokenizer import CharTokenizer


class TestCharTokenizer(TestCase):
    def setUp(self):
        self.text = "بۈگۈن ئۇيغۇر تىلى كۈنى بولۇپ، دۇنيانىڭ ھەرقايسى جايلىرىدىكى ئۇيغۇرلار بۇ كۈننى ئۆزگىچە خاتىرىلەيدۇ."

    def test_with_punctuation(self):
        tokenizer = CharTokenizer()
        tokens_punc = tokenizer.tokenize(text=self.text, keep_punctuation=True)
        print("No punctuation:", tokens_punc)

    def test_with_no_punctuation(self):
        tokenizer = CharTokenizer()
        tokens_with_punc = tokenizer.tokenize(text=self.text, keep_punctuation=False)
        print("With punctuation:", tokens_with_punc)
