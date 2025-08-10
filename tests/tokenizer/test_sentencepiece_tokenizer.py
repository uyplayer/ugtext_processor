import os
import shutil
import tempfile
from unittest import TestCase

from ugtext_processer.tokenizer.sentencepiece_tokenizer import SentencePieceTokenizer
from conf.path_config import data_dir


class TestSentencePieceTokenizer(TestCase):
    def setUp(self):

        self.temp_dir = tempfile.mkdtemp()
        self.corpus_path = os.path.join(data_dir, "corpus.txt")
        self.model_dir = os.path.join(self.temp_dir, "model")
        os.makedirs(self.model_dir, exist_ok=True)


    def tearDown(self):

        shutil.rmtree(self.temp_dir)

    def test_train_and_tokenize(self):
        tokenizer = SentencePieceTokenizer()
        tokenizer.train_tokenizer(self.corpus_path, save_dir=self.model_dir, model_prefix="test_spm", vocab_size=5000)

        tokens = tokenizer.tokenize("مەن كىتاب ئوقۇيمەن")
        print("Tokens:", tokens)
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    def test_load_model(self):
        tokenizer = SentencePieceTokenizer()
        tokenizer.train_tokenizer(self.corpus_path, save_dir=self.model_dir, model_prefix="test_spm", vocab_size=11833)

        model_path = os.path.join(self.model_dir, "test_spm.model")

        new_tokenizer = SentencePieceTokenizer()
        new_tokenizer.load_tokenizer(model_path)

        tokens = new_tokenizer.tokenize("ئۇ كىتاب ئوقۇدى")
        print("Tokens after loading model:", tokens)
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    def test_verbose(self):
        tokenizer = SentencePieceTokenizer()
        tokenizer.train_tokenizer(self.corpus_path, save_dir=self.model_dir, model_prefix="test_spm", vocab_size=11833)

        output = tokenizer.verbose()
        print("Verbose output:", output)
        self.assertIn("SentencePieceTokenizer", output)
        self.assertIn("Vocabulary size", output)

    def test_tokenize_without_model(self):
        tokenizer = SentencePieceTokenizer()
        with self.assertRaises(ValueError):
            tokenizer.tokenize("مەن يولغا چىقتىم")

    def test_load_invalid_path(self):
        tokenizer = SentencePieceTokenizer()
        with self.assertRaises(FileNotFoundError):
            tokenizer.load_tokenizer("nonexistent/path.model")


if __name__ == "__main__":
    import unittest
    unittest.main()
