from ugtext_processer.normalizer.currency import UyghurCurrency


def run_tests():
    conv = UyghurCurrency()

    test_cases = [
        "$100",
        "€250",
        "¥300",
        "₺75",
        "USD400",
        "EUR200",
        "ئۇ $50 ۋە EUR100 بىلەن سېتىۋالدى",
        "$123.45 ۋە ¥88.88",
        "TRY900 JPY1000"
    ]

    for i, text in enumerate(test_cases, 1):
        result = conv.convert_currency_symbol_to_text(text)
        print(f"[Test {i}] Original: {text}")
        print(f"         Converted: {result}")
        print("-" * 50)

if __name__ == '__main__':
    run_tests()
