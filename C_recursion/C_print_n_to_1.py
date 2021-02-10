def method1(n: int) -> list:
    return [i for i in range(n, 0, -1)]


def method2(n: int) -> list:
    return [n - x for x in range(n)]


def method3(n: int) -> int:
    print(*range(n, 0, -1))


def method4(n: int) -> int:
    while n > 0:
        print(n)
        n -= 1


if __name__ == "__main__":
    
    from timeit import timeit
    print(timeit(lambda: method1(10), number=10000)) 
    print(timeit(lambda: method2(10), number=10000)) 
    print(timeit(lambda: method3(10), number=10000)) 
    print(timeit(lambda: method4(10), number=10000)) 
    
