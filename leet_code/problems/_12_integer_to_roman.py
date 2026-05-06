def int_to_roman(num):

    roman_dict = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    sym = []
    for k, v in roman_dict.items():
        print(f"num: {num}\n")
        while num > 0:
            if v <= num:
                sym.append(k)
                num -= v
            else:
                break

    return "".join(sym)


num = 3749

print(int_to_roman(num))
