# Patrick Canto de Carvalho - 201935026

import math
import random
import time


def generate_prime():
    min = 10000

    shift = math.floor(random.random() * 100000)
    count = 0

    while True:
        number = min + shift + count
        if check_prime(number) and number % 4 == 3:
            return min + shift + count

        count += 1


def check_prime(number):
    root = int(math.floor(math.sqrt(number)))

    for i in range(2, root + 1):
        # print(f"{number}%{i}=: {number % i}")

        if number % i == 0:
            return False

    return True


def run_bbs(s, n, length):
    x = (s ** 2) % n
    res = 0
    b = [""] * length
    for i in range(length):
        x = (x ** 2) % n
        res = res + (x % 2) * (2 ** i)
        b[i] = str(x % 2)
    return b


def main():
    p = generate_prime()
    q = generate_prime()
    s = 101355
    random.seed(time.time())

    print(f"p: {p}  q:{q}   s:{s}   n:{p * q}")

    res = run_bbs(s, p * q, 10000)

    print(f"result: {''.join(res)}")


if __name__ == "__main__":
    main()
