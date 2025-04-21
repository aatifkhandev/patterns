# Print name 5 times


def PrintName(name,count):
    if count == 5:
        return
    print(name)
    count+=1
    PrintName(name,count)
    

PrintName("aatif",0)


# Print Linearly from 1 to N

def Linearly(i,n):
    if i>n:
        return
    print(i)
    # i+=1
    Linearly(i+1,n)
    
Linearly(1,10)



# Print Linearly from N to 1

def NonLinearly(i,n):
    if i<1:
        return
    print(i)
    # i+=1
    NonLinearly(i-1,n)
    
NonLinearly(5,1)

