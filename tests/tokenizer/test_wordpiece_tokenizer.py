import os
import shutil
import tempfile
from unittest import TestCase

import pytest

from ugtext_processor.tokenizer.wordpiece_tokenizer import WordpieceTokenizer

from path_config   import data_dir


class TestWordPieceTokenizer(TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.corpus_path = os.path.join(data_dir, "corpus.txt")
        self.save_dir = os.path.join(self.temp_dir, "word_piece_tokenizer_model")

    @pytest.mark.skip(reason="ignore tearDown")
    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    @pytest.mark.skip(reason="ignore test_train_and_tokenize")
    def test_train_and_tokenize(self):
        tokenizer = WordpieceTokenizer()
        tokenizer.train_tokenizer(self.corpus_path, vocab_size=50000, save_dir=self.save_dir)

        tokens = tokenizer.tokenize("مەن كىتاب ئوقۇيمەن")
        print("Tokens:", tokens)
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    @pytest.mark.skip(reason="ignore test_save_and_load_tokenizer")
    def test_save_and_load_tokenizer(self):
        tokenizer = WordpieceTokenizer()
        tokenizer.train_tokenizer(self.corpus_path, vocab_size=100, save_dir=self.save_dir)

        save_path = os.path.join(self.save_dir, "tokenizer.json")
        tokenizer.save_tokenizer(save_path)
        self.assertTrue(os.path.exists(save_path))

        new_tokenizer = WordpieceTokenizer()
        new_tokenizer.load_tokenizer(save_path)
        tokens = new_tokenizer.tokenize("ئۇ بازارغا كېتىدۇ")
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0)

    @pytest.mark.skip(reason="ignore test_verbose")
    def test_verbose(self):
        tokenizer = WordpieceTokenizer()
        tokenizer.train_tokenizer(self.corpus_path, vocab_size=100, save_dir=self.save_dir)

        summary = tokenizer.verbose()
        print("Tokenizer Summary:", summary)
        self.assertIn("WordPieceTokenizer", summary)
        self.assertIn("vocab size", summary)

    @pytest.mark.skip(reason="ignore test_tokenize_without_training_or_loading")
    def test_tokenize_without_training_or_loading(self):
        tokenizer = WordpieceTokenizer()
        with self.assertRaises(ValueError):
            print(tokenizer.tokenize("مەن يولغا چىقتىم"))

    @pytest.mark.skip(reason="ignore test_load_invalid_path")
    def test_load_invalid_path(self):
        tokenizer = WordpieceTokenizer()
        with self.assertRaises(FileNotFoundError):
            tokenizer.load_tokenizer("invalid_path/tokenizer.json")
