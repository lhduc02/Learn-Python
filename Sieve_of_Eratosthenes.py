"""
Tìm và liệt kê các số nguyên tố có trong đoạn [1,n].

Input: Dòng duy nhất chứa số nguyên n, với 1≤n≤10^6
Output: In ra các số nguyên tố trong đoạn [1, n]. Nếu không có số nguyên tố nào thì in ra 0
"""

def find_prime_numbers(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

n = int(input("Nhập số nguyên n: "))

prime_numbers = find_prime_numbers(n)

if len(prime_numbers) > 0:
    print("Các số nguyên tố trong đoạn [1, {}]:".format(n))
    print(*prime_numbers)
else:
    print(0)
