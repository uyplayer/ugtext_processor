import unittest
from ugtext_processor.phonemizer import UgPhonemizer

class TestUgPhonemizer(unittest.TestCase):

    def test_uly_basic(self):
        p = UgPhonemizer(mod=UgPhonemizer.Mod.ULY)
        text = "ئەسسالامۇ ئەلەيكۇم"
        expected = ['e', '_', 's', '_', 's', '_', 'a', '_', 'l', '_', 'a', '_', 'm', '_', 'u', '_',
                    '|', 'e', '_', 'l', '_', 'e', '_', 'y', '_', 'k', '_', 'u', '_', 'm']
        result = p.phonemizer(text)
        print("ULY basic →", result)


    def test_ipa_basic(self):
        p = UgPhonemizer(mod=UgPhonemizer.Mod.IPA)
        text = "ئەسسالامۇ"
        result = p.phonemizer(text)
        print("IPA basic →", result)


    def test_custom_punctuation(self):
        pattern = r"[،؛!]"
        p = UgPhonemizer(mod=UgPhonemizer.Mod.ULY, punctuation_pattern=pattern)
        text = "ياخشىمۇسىز؟، ئەسسالامۇ!"
        result = p.phonemizer(text)
        print("Custom punctuation →", result)


    def test_blank_control(self):
        p = UgPhonemizer(mod=UgPhonemizer.Mod.ULY)
        text = "ئەسسالامۇ"
        result = p.phonemizer(text)
        print("Blank=False →", result)


    def test_empty_text(self):
        p = UgPhonemizer()
        result = p.phonemizer("")
        print("Empty input →", result)


    def test_word_boundary_marker(self):
        p = UgPhonemizer(mod=UgPhonemizer.Mod.ULY)
        text = "ياخشىمۇسىز ئەپەندىم"
        result = p.phonemizer(text)
        print("Word boundary →", result)


if __name__ == '__main__':
    unittest.main()
