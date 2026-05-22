# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


class Ex7:
    def reverse_string_with_for(self, s: list) -> str:
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        for i in range(1, len(s) // 2 + 1):

            s[i - 1], s[len(s) - i] = (
                s[len(s) - i],
                s[i - 1],
            )

        return "".join(s)

    def reverse_string_with_while(self, s: list) -> str:
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        i = 1
        while i <= len(s) and len(s[i - 1 : len(s) - i + 1]) >= 1:

            s[i - 1], s[len(s) - i] = (
                s[len(s) - i],
                s[i - 1],
            )

            i += 1

        return "".join(s)


if __name__ == "__main__":

    s = list("hello")
    ex = Ex7()
    print(ex.reverse_string_with_for(s))
    print(ex.reverse_string_with_while(s))
