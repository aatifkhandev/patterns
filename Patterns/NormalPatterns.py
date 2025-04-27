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
    
    
    
    
RightAngled(5)