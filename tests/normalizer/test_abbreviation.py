from ugtext_processer.normalizer.abbreviation import UyghurAbbreviation



def run_tests():
    normalizer = UyghurAbbreviation()

    test_cases = [
        ("kg بۇ بىرلىككە قاراڭ", "بۇ بىرلىككە قاراڭ كىلوگىرام"),
        ("cm kg بۇ بىرلىككە قاراڭ", "بۇ بىرلىككە قاراڭ سېنتىمىتىر كىلوگىرام"),
        ("بۇ بىرلىككە قاراڭ KG", "بۇ بىرلىككە قاراڭ كىلوگىرام"),
        ("بۇ بىرلىككە قاراڭ Cm", "بۇ بىرلىككە قاراڭ سېنتىمىتىر"),
        ("kg cm kg cm", "سېنتىمىتىر كىلوگىرام"),
        ("ئۇ 5kg ئېلىپ كەلدى", "ئۇ 5kg ئېلىپ كەلدى"),
    ]

    for i, (text, expected) in enumerate(test_cases, 1):
        result = normalizer.convert(text)
        print(f"input:    {text}")
        print(f"result:   {result}")
        print("-" * 50)

if __name__ == '__main__':
    run_tests()
