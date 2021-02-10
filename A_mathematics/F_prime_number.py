def method1(n: int) -> bool:
    if n > 1:
        for i in range(2, n + 1):
            return False if n % i == 0 and i != n and i != 1 else True
    else:
        return False


def method2(n: int) -> bool:
    from itertools import count, islice

    def prime(n: int) -> bool:
        return n > 1 and all(n % i for i in islice(count(2), int((n) ** 0.5 - 1)))

    return prime(n)


if __name__ == "__main__":

    from timeit import timeit
    print(timeit(lambda: method1(10), number=10000)) 
    print(timeit(lambda: method2(10), number=10000)) 

