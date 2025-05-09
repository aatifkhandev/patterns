
# # def f(count):
# #     if count>=10:
# #         return
# #     print(count)
# #     count+=1
    
# #     f(count)
    

# # f(count)

# def printName(count,name):
#     if count==5:
#         return
    
#     print(name)
    
#     printName(count+1,name)
    


# # printName(0,"aatif")

# # Non linear from n to 1 -> 10 - 1

# def nonL(i,n):
#     if i<=1:
#         return
#     print(i)
#     nonL(i-1,n)
    

# n = int(input("enter a number"))
# nonL(10,n)








# 






# def NonLinearBackTrack(i,n):
#     if(i>n):
#         return
    
#     NonLinearBackTrack(i+1,n)
#     print(i)
    

# NonLinearBackTrack(1,3)



def sumRecursive(i,sum): # parameter
    if i<1:
        print(sum)
        return
    
    sumRecursive(i+1,sum+i)
    
    

sumRecursive(1,5)