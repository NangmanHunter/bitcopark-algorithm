# Recursive
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

# Memorization
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fib_memo(n-1, memo)+fib_memo(n-2,memo)
    return memo[n]


import time
n=40
start=time.time()
print(f"일반재귀결과: {fib(n)}")
print(f"일반재귀시간: {time.time() - start:.2f}초")

start=time.time()
print(f"메모이제이션결과: {fib_memo(n)}")
print(f"메모이제이션시간: {time.time() - start:.2f}초")
