class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n < 1:
            return []
        if n == 1:
            return ["1"]
        if n == 2:
            return ["1", "2"]

        answer = ["1", "2"]  # Initialize with known values
        for i in range(3, n + 1):
            str_answer = ""
            if i % 3 == 0:
                str_answer += "Fizz"
            if i % 5 == 0:
                str_answer += "Buzz"
            if not str_answer:
                str_answer += str(i)
            answer.append(str_answer)
        return answer
