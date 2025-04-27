# Pattern-1: Rectangular Star Pattern

# * * * *
# * * * *
# * * * *

def rectangularPattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end='')
        print()
        
    
    
# rectangularPattern(5)


# Pattern-2: Right-Angled Triangle Pattern

# *
# * *
# * * *
# * * * *
# * * * * *

def RightAngled(n):
    
    for i in range(n):
        for j in range(i+1):
            print("*",end='')
        print()
    
    
    
    
# RightAngled(5)



# Pattern - 3: Right-Angled Number Pyramid
# 1
# 1 2 
# 1 2 3

def RightNumbered(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
    
    
    
# RightNumbered(5)

