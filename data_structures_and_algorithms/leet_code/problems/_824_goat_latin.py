"""
If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
"""


def toGoatLatin(sentence):
    """
    :type sentence: str
    :rtype: str
    """

    vowels = ["a", "e", "i", "o", "u"]

    def process_word(word):

        if word[0].lower() in vowels:
            word += "ma"  # append "ma" to the end of the word.
        else:
            word = (
                word[1:] + word[0] + "ma"
            )  # remove the first letter and append it to the end, then add "ma".
        return word

    sentence_list = sentence.split(" ")
    print(sentence_list)
    for i, word in enumerate(sentence_list):
        sentence_list[i] = process_word(word) + (i + 1) * "a"

    return " ".join(sentence_list)


sentences = ["I speak Goat Latin", "Each word"]
for sentence in sentences:
    print(toGoatLatin(sentence))
