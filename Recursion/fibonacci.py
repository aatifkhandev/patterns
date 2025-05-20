# Optimized code

def fib(n):
    if n<=1:
        return n
    last = fib(n-1)
    secondLast = fib(n-2)
    return last+secondLast

print(fib(4))

# Better code - whole series

def fibonacci_series(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    
    return series


# print(fibonacci_series(5))

# Naive Approach -> using for loop
def FibUsingLoop(n):
    if n==0:
        return 0
    if n==1:
        return 1
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]
        
        
# print(FibUsingLoop(4))
        
