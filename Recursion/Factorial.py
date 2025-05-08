# Factorial using Parameter version

def factorial(i,mul):
    if i==0:
        return mul
    
    return factorial(i-1,mul*i)


    

print(factorial(3,1))


# using functional method
def factorialF(n):
    if n==0:
        return 1
    return n*factorialF(n-1)


print(factorialF(5))