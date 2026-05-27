"""
Please write functions to satisfy the following requirements
Please write unit tests for the functions

For words that begin with a consonant, move all letters before the first vowel
(a, e, i, o, u) to the end and append “ay” as the suffix.

For words that begin with a vowel, leave the vowel in place and append “yay” as
the suffix.
"""


class Ex11:

    def yay(self, s: str) -> str:

        vowels = ("a", "e", "i", "o", "u")

        for i, char in enumerate(s):
            if s[0].lower() not in vowels:
                if char in vowels:
                    return s[i:] + s[:i] + "ay"
            else:
                return s + "yay"


if __name__ == "__main__":
    ex = Ex11()

    s = "Pig"
    print(ex.yay(s))
