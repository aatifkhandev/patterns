# def my_sum(i,n):
#     ans = 0
#     for i in range(i,n+1):
#         ans+=i
#     return ans


# print(my_sum(1,5))


def sumRecursive(i,n):
   
    if i>n:
        return 0
    sumRecursive(i+1,n)
    return i+sumRecursive(i+1,n)


print(sumRecursive(1,5))
    
    
