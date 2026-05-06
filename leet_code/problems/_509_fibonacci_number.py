def fib1(n):
    """
    :type n: int
    :rtype: int
    """
    memo = {0: 0, 1: 1}

    def helper(n):
        if n in memo:
            return memo[n]
        seq = helper(n - 2) + helper(n - 1)
        memo[n] = seq
        return memo[n]

    return helper(n)


def fib2(n):
    def helper(n, memo):
        if n in memo:
            return memo[n]
        seq = helper(n - 2, memo) + helper(n - 1, memo)
        memo[n] = seq
        return memo[n]

    memo = {0: 0, 1: 1}
    return helper(n, memo)
