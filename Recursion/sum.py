# def my_sum(i,n):
#     ans = 0
#     for i in range(i,n+1):
#         ans+=i
#     return ans


# print(my_sum(1,5))


def sumRecursive(i,sum): # parameter
    if i<1:
        print(sum)
        return
    
    sumRecursive(i-1,sum+i)
    
    
# n = int(input("Enter a number"))
# sumRecursive(n,0)
        

def FunctionalSum(n) :  # Functional recursion 
    if n==0:
        return 0
    
    return n+FunctionalSum(n-1)


print(FunctionalSum(5))
    
    
