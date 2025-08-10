from unittest import TestCase

from ugtext_processor.tokenizer.word_tokenizer import WordTokenizer


class TestWordTokenizer(TestCase):
    def setUp(self):
        self.tk = WordTokenizer()

    def test_with_punctuation(self):
        text_tmp = "بۈگۈن ئۇيغۇر تىلى كۈنى بولۇپ، دۇنيانىڭ ھەرقايسى جايلىرىدىكى ئۇيغۇرلار بۇ كۈننى ئۆزگىچە خاتىرىلەيدۇ."
        tokens_no_punc = self.tk.tokenize(text_tmp, keep_punctuation=False)
        print("No punctuation:", tokens_no_punc)

    def test_with_no_punctuation(self):
        text_tmp = "بۈگۈن ئۇيغۇر تىلى كۈنى بولۇپ، دۇنيانىڭ ھەرقايسى جايلىرىدىكى ئۇيغۇرلار بۇ كۈننى ئۆزگىچە خاتىرىلەيدۇ."
        tokens_with_punc = self.tk.tokenize(text_tmp, keep_punctuation=True)
        print("With punctuation:", tokens_with_punc)
