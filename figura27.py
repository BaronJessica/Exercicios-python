"""def fibo(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)"""

def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
for i in range(10):
    print(rec_fib(i))








