# def my_sum(i,n):
#     ans = 0
#     for i in range(i,n+1):
#         ans+=i
#     return ans


# print(my_sum(1,5))


def sumRecursive(i,sum):
    if i<1:
        print(sum)
        return
    
    sumRecursive(i-1,sum+i)
    
    
n = int(input("Enter a number"))
sumRecursive(n,0)
        
    
    
