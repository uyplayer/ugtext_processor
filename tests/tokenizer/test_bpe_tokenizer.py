import os
import tempfile
from pathlib import Path
from unittest import TestCase

import pytest

from ugtext_processor.tokenizer.bpe_tokenizer import BpeTokenizer


from path_config import data_dir


class TestBpeTokenizer(TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.corpus_path = Path(data_dir) / "corpus.txt"
        self.model_path = Path(self.temp_dir.name) / "test_bpe_model.json"
        print(f"Temporary directory created at: {self.temp_dir.name}")

    @pytest.mark.skip(reason="ignore test_initialization")
    def test_initialization(self):
        """
        Test tokenizer initialization and default special tokens
        """
        tokenizer = BpeTokenizer()
        self.assertIsNone(tokenizer.tokenizer)
        self.assertListEqual(tokenizer.special_tokens, ["<unk>", "<pad>", "<bos>", "<eos>", "<mask>", "<cls>", "<sep>"])

    @pytest.mark.skip(reason="ignore test_initialization_with_custom_special_tokens")
    def test_initialization_with_custom_special_tokens(self):
        """
        Test tokenizer initialization with custom special tokens
        """
        custom_tokens = ["[UNK]", "[PAD]", "[START]", "[END]"]
        tokenizer = BpeTokenizer(special_tokens=custom_tokens)
        self.assertListEqual(tokenizer.special_tokens, custom_tokens)

    @pytest.mark.skip(reason="ignore test_train_and_tokenize")
    def test_train_and_tokenize(self):
        """
        Test the full training and tokenization process
        """
        tokenizer = BpeTokenizer()
        self.assertIsNone(tokenizer.tokenizer, "Tokenizer should be None before training")


        trained_tokenizer = tokenizer.train_tokenizer(str(self.corpus_path), str(self.model_path))
        self.assertIsNotNone(trained_tokenizer, "Training should return a valid tokenizer instance.")
        self.assertTrue(self.model_path.is_file(), "Model file should be created after training.")
        self.assertGreater(tokenizer.tokenizer.get_vocab_size(), 0, "Vocabulary size should be greater than zero.")

        text = "بۇ بىر سىناق."
        tokens = tokenizer.tokenize(text)
        print(f"Tokens for '{text}': {tokens}")
        self.assertIsInstance(tokens, list)
        self.assertGreater(len(tokens), 0, "Tokenization should produce a non-empty list of tokens.")
        self.assertTrue(all(isinstance(t, str) for t in tokens), "All tokens should be strings.")

    @pytest.mark.skip(reason="ignore test_save_and_load")
    def test_save_and_load(self):
        """
        Test saving a trained tokenizer and loading it back
        """

        tokenizer1 = BpeTokenizer()
        tokenizer1.train_tokenizer(str(self.corpus_path), str(self.model_path))
        tokenizer1.save_tokenizer(str(self.model_path))


        tokenizer2 = BpeTokenizer()
        tokenizer2.load_model(str(self.model_path))


        self.assertIsNotNone(tokenizer2.tokenizer, "Loaded tokenizer should not be None.")
        self.assertEqual(tokenizer1.tokenizer.get_vocab(), tokenizer2.tokenizer.get_vocab(), "Vocabularies should match.")

        text = "بۇ بىر سىناق."
        tokens1 = tokenizer1.tokenize(text)
        tokens2 = tokenizer2.tokenize(text)
        print(f"Tokens from original tokenizer: {tokens1}")
        print(f"Tokens from loaded tokenizer: {tokens2}")
        self.assertEqual(tokens1, tokens2, "Tokenization results from original and loaded models should be identical.")

    @pytest.mark.skip(reason="ignore test_tokenize_uninitialized_raises_error")
    def test_tokenize_uninitialized_raises_error(self):
        """
        Test that tokenizing with an uninitialized tokenizer raises a RuntimeError
        """
        tokenizer = BpeTokenizer()
        with self.assertRaisesRegex(RuntimeError, "Tokenizer has not been trained or loaded yet."):
            tokenizer.tokenize("بۇ بىر سىناق.")


    @pytest.mark.skip(reason="ignore test_tokenize_with_unknown_words")
    def test_tokenize_with_unknown_words(self):
        """
        Test tokenizing text containing words not in the vocabulary
        """
        tokenizer = BpeTokenizer()
        tokenizer.train_tokenizer(str(self.corpus_path), str(self.model_path))

        text_with_unknowns = "A quantum xylophone appeared."
        tokens = tokenizer.tokenize(text_with_unknowns)
        print(f"Tokens for '{text_with_unknowns}': {tokens}")

        self.assertGreater(len(tokens), 0)
        self.assertIsInstance(tokens, list)
