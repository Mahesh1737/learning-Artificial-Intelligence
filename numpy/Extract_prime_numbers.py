import numpy as np

arr = np.array([2,3,4,5,10,11,17,20,23])

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(np.sqrt(n))+1):
        if n%i==0:
            return False
    return True

prime_check = np.vectorize(is_prime)

prime_numbers = arr[prime_check(arr)]

print("Prime numbers: ", prime_numbers)