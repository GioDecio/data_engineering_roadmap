"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

"""

def lengthOfLastWord(s):
   """
    :type s: str
    :rtype: int
   """

   cnt = 0
   for i in range(len(s)-1, -1, -1):
      if s[i] !=' ':
         cnt+=1
      if s[i]== ' ' and cnt != 0:
         return cnt
   return cnt
      
          


s = 'Hello World'
print(lengthOfLastWord(s))
