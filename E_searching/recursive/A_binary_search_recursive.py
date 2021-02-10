def method1_recursive(l: list, low: int, high: int, x: int) -> int:
    if high >= low:
        mid = (high + low) // 2
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            return method1_recursive(l, low, mid - 1, x)
        else:
            return method1_recursive(l, mid + 1, high, x)
    else:
        return -1
    return method1_recursive(l, 0, len(l) - 1, x)


if __name__ == "__main__":
    
    n = 9999
    l = [i for i in range(10000)] 
    from timeit import timeit
    print(timeit(lambda: method1_recursive(l, 0, len(l)-1, n), number=10000)) 
    
