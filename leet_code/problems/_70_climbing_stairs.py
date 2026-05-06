def climbing_recursive(n): 
    if n==1:
        return 1
    if n==2:
        return 2
    return climbing_recursive(n-2) + climbing_recursive(n-1)


def climbing_memo(n):
        
        memo = {1:1, 2:2}

        def f(n):
             if n in memo:
                return memo[n]
             else:
                memo[n] = f(n-2) + f(n-1)
                return memo[n]
        return f(n)



n = 5
print(climbing_memo(n))
