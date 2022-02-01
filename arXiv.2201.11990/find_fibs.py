def find_3_or_7_divisible_fibs(n):
    """Find all the Fibonacci numbers below n that are divisible by 3 or divisible by 7.
    """
    return [f for f in find_fibs(n) if f % 3 == 0 or f % 7 == 0]

def find_fibs(n):
    """Find all Fibonacci numbers below n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b