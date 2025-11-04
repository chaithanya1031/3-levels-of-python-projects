def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(10))
def print_primes_upto(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=' ')
print_primes_upto(10)
def primes_in_range(a, b):
    primes = []
    for i in range(a, b + 1):
        if is_prime(i):
            primes.append(i)
    return primes
print(primes_in_range(1,10))