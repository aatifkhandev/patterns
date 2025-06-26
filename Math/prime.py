# Input:N = 2
               
# Output:True
                
# 2 is a prime number because it has two divisors: 1 and 2 (the number itself).

import math

def prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    
    if cnt ==2:
        return True
    else:
        return False
    


def primeOptimized(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1  
            if i != n // i:  
                cnt += 1  
    
   
    return cnt == 2

print(primeOptimized(11))