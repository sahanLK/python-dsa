
def factorial(num: int):
    if num == 1:
        return 1
    print(num)
    out = num * factorial(num - 1)
    print("Out: ", out)
    return out

print(factorial(5))


"""
Call Stack:

1
2 * factorial(1) = 2
3 * factorial(2) = 6
4 * factorial(3) = 24
5 * factorial(4) = 120
"""