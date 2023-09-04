def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def calc_prime_divisors(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            divisors.append(i)
    return divisors

def find_quadratic_prime_divisors(a, b, c):
    discriminant = b**2 - 4*a*c
    roots = []
    if discriminant >= 0:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        roots = [root1, root2]
    
    prime_divisors = set()
    for root in roots:
        if root >= 0 and root == int(root):
            prime_divisors.update(calc_prime_divisors(int(root)))
    return sorted(list(prime_divisors))



# Read the matrix from the text file

a,b,c = map(int,"1 -338 22477".strip().split())
print(find_quadratic_prime_divisors(a, b, c))