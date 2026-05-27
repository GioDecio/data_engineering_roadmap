# Coding Exercise
# 1) Create a function that accepts the following sentences and returns the
# corresponding encoded message:
# Input: pleased to meet you
# Output: easedplay otay eetmay ouyay
# Input: how much does it cost
# Output: owhay uchmay oesday ityay ostcay
# Input: i would rather be at the beach
# Output: iyay ouldway atherray ebay atyay ethay eachbay
# Input: a tree whose elements have at most two children is called a binary
# tree
# Output: ayay eetray osewhay elementsyay avehay atyay ostmay otway ildrenchay
# isyay alledcay ayay inarybay eetray


# 2) Update the function to match the letter casing of the original sentence with the
# encoded sentence. For example, if the word“Pig” is passed, then “Igpay”
# should be returned. If the word“LATIN” is passed then “ ATINLAY” should be
# returned.
# Input: Pleased to meet you
# Output: Easedplay otay eetmay ouyay
# Input: Do you speak Pig Latin
# Output: Oday ouyay eakspay Igpay Atinlay
# Input: Time flies when you are having fun
# Output: Imetay iesflay enwhay ouyay areyay avinghay unfay
# Input: A tree whose elements have at most two children is called a BINARY
# TREE
# Output: Ayay eetray osewhay elementsyay avehay atyay ostmay otway ildrenchay
# isyay alledcay ayay INARYBAY EETRAY


class Ex12:

    def _yay(self, s: str) -> str:

        vowels = ("a", "e", "i", "o", "u")

        for i, char in enumerate(s):
            if s[0].lower() not in vowels:
                if char in vowels:
                    return s[i:] + s[:i] + "ay"
            else:
                return s + "yay"

    def _upper_check(self, new_s, _d, word):
        for k, char in enumerate(word):
            if k in _d:
                if _d[k]:
                    new_s = new_s + char.upper()
                else:
                    new_s = new_s + char
            else:
                new_s = new_s + char

        return new_s

    def encoded_language(self, s: str) -> str:
        s_list = s.split(" ")
        for i, word in enumerate(s_list):
            s_list[i] = self._yay(word)
        return " ".join(s_list)

    def encoded_language2(self, s: str) -> str:
        """More general approach where not only title or all upper case are
        considered, but also circumstances where the upper case can be in the middle of the
        word."""

        # TODO Address cases where there is a word made by one capital letter only.

        s_list = s.split(" ")

        for i, orig_word in enumerate(s_list):  # loop across each word of the sentence
            _d = {}

            for j, char in enumerate(
                orig_word
            ):  # loop across each word in the sentence
                _d[j] = (
                    char.isupper()
                )  # Create a dictionary that keeps track of the index and case of the letter at that index in the original word

            s_list[i] = self._yay(
                orig_word.lower()
            )  # #apply the original transformation, this modifies the original s_list

            new_word = ""
            if orig_word[0] not in ["a", "e", "i", "o", "u"]:
                # check the first character
                if (
                    orig_word.isupper()
                ):  # if it is all upper, then make sure the last three letters are upper too
                    new_word = s_list[i].upper()
                else:  # Make the letter upper according to _d values for a given position
                    new_word = self._upper_check(new_word, _d, s_list[i])
            else:
                if orig_word.isupper():
                    new_word = s_list[i].upper()
                else:
                    new_word = self._upper_check(new_word, _d, s_list[i])
            s_list[i] = new_word  # Overwrite the new value

        return " ".join(s_list)


if __name__ == "__main__":
    ex = Ex12()

    s = "pErLa"
    # print(ex.encoded_language(s))
    print(ex.encoded_language2(s))
