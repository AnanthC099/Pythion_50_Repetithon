"""
Simplified version of test_logger.py

Uses the simplified logger decorator to test various function calls.
"""

from logger_simple import logger
from time import sleep


@logger
def compute1(a, b, c):
    return (a - b) * (b + c) + (c - a)


@logger
def compute2(x, y):
    return x**2 - y**2


@logger
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Test calls
ret = compute1(10, b=20, c=30)
print("ret:", ret)

sleep(1)
ret = compute2(3, y=1)
print("ret:", ret)

sleep(1)
ret = factorial(n=5)
print("ret:", ret)

sleep(1)
ret = compute1(6, 3, 1)
print("ret:", ret)
