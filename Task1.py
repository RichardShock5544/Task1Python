from collections import Counter
symbols = input()
def change_symbols(symbols: str) -> str:
    low_symbols = symbols.lower()
    counter = Counter(low_symbols)
    return ''.join([')' if counter.get(c) > 1 else '(' for c in low_symbols])
print(change_symbols(symbols))
