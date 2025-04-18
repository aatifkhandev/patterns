
# count = 0
# def Aatif(count):
#     if count>=10:
#         return
#     count+=1
    
#     print(count)
#     Aatif(count)
    
# Aatif(count)

count = 0

def f(count):
    if count>=10:
        return
    print(count)
    count+=1
    
    f(count)
    

f(count)