# Problema: data una stringa, contami quante volte appare la lettera 'a'.


def count_char_occurrence(_string: str, _char: str) -> int:

    d = {}

    for c in _string:
        if c in d:

            d[c] += 1
        else:
            d[c] = 1

    return d.get(_char, 0)
