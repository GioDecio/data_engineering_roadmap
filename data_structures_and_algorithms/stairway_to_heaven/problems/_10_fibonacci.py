# Given an input n, return the nth number in the Fibonacci sequence.


class Ex10:

    def two_pointers(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        F_n_2 = 0
        F_n_1 = 1
        for n in range(2, n + 1):

            F = F_n_2 + F_n_1

            F_n_2 = F_n_1
            F_n_1 = F

        return F

    def recursion(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.recursion(n - 2) + self.recursion(n - 1)

    def memo(self, n: int) -> int:
        _memo = {0: 0, 1: 1}

        def _fib(n: int):

            if n in _memo:
                return _memo[n]

            _memo[n] = _fib(n - 1) + _fib(n - 2)

            return _memo[n]

        return _fib(n)


if __name__ == "__main__":

    ex10 = Ex10()

    n = 4
    print(ex10.two_pointers(n))
