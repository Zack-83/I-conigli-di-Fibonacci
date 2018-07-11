def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        prnit(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    """
    As described by Fibonacci et al. (1201)
    
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#if __name__ == "__main__":
#    import sys
#    import numpy
#    fib(int(sys.argv[1]))
#    print(fib2(int(sys.argv[1])))
#    print(numpy.array(fib2(int(sys.argv[1]))))
