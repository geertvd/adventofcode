import math


def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

input = 36000000
presents = 0
house_number = 1
while presents < input:
    presents = sum(list(divisorGenerator(house_number))) * 10
    house_number += 1

print house_number - 1
