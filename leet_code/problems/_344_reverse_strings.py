"""
Write a function that reverses a string. 
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        # Funzione helper ricorsiva con indici
        def reverse_helper(start, end):
            if start >= end:
                return

            # Scambia i caratteri nell'array
            s[start], s[end] = s[end], s[start]

            # Chiamata ricorsiva con indici aggiornati
            reverse_helper(start + 1, end - 1)

        # Avvia la ricorsione con indici iniziali
        reverse_helper(0, len(s) - 1)


s = "h e l l o".split(" ")
