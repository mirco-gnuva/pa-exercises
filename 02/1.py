# Write the solutions for the following quizzes by using functional programming:
#  1. Sum all the natural numbers below one thousand that are multiples of 3 or 5.
#  2. Calculate the smallest number divisible by each of the numbers 1 to 20.
#  3. Calculate the sum of the figures of 2^1000
#  4. Calculate the first term in the Fibonacci sequence to contain 1000 digits.

from functools import reduce

def ex_1():
    return sum(i for i in range(1000) if not (i % 3 or i % 5))


def ex_2():    
    from math import gcd

    return reduce(lambda a, b: a * b // gcd(a,b), range(1, 21))

def ex_3():
    return sum(int(c) for c in str(2**1000))

def ex_4():
    def fib():
        a = b = 1

        while True:
            yield a

            a, b = b, a + b

    return next(filter(lambda x: len(str(x)) >= 1000, fib()))


if __name__ == '__main__':
    print(ex_1())
    print(ex_2())
    print(ex_3())
    print(ex_4())