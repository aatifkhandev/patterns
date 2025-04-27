# Pattern-1: Rectangular Star Pattern

# * * * *
# * * * *
# * * * *

def rectangularPattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end='')
        print()
        
    
    
rectangularPattern(5)