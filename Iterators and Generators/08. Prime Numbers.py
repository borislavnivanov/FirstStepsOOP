def get_primes(numbers: list):
    for el in numbers:
        if el < 2:
            continue
        for i in range(2, el):
            if el % i == 0:
                break
        else:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
