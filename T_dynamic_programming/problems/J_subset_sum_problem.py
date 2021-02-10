def method1(set, n, sum):

    if sum == 0:
        return True
    if n == 0:
        return False

    
    
    if set[n - 1] > sum:
        return method1(set, n - 1, sum)

    
    
    
    
    return method1(set, n - 1, sum) or method1(set, n - 1, sum - set[n - 1])


if __name__ == "__main__":
    
    from timeit import timeit

    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(set)
    print(
        timeit(lambda: method1(set, n, sum) == True, number=10000)
    )  
    
