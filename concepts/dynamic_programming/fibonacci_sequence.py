
"""
Fibonacci sequence qithout memoization
"""
counter = 0

def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

"""
Fibonacci sequence with Memoization
"""
memo = [None] * 100
def fib_with_memo(n):
    if memo[n]:
        return memo[n]

    if n == 0 or n == 1:
        return n

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


"""
Fibonacci sequence bottom-up
"""
counter = 0
def fib_bottom_up(n):
    fib_list = [0, 1]
    global counter

    for index in range(2, n + 1):
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]


if __name__ == "__main__":
    print(fib_bottom_up(10))


