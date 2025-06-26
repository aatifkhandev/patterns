# N = 12 
# o/p = 1,2,3,4,6,12
import math

def divisor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)


def divisorOptimized(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            divisors.append(i)
        
        if i!=n//i:
            divisors.append(n//i)
        
    divisors.sort()
    print(divisors)
    




divisorOptimized(12)