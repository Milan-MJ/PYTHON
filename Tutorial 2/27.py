# Write a Python program to read list of positive integers and separate the prime and composite numbers
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

nums = list(map(int, input("Enter numbers: ").split()))
primes = [n for n in nums if is_prime(n)]
composites = [n for n in nums if n not in primes]
print("Primes:", primes, "\nComposites:", composites)
