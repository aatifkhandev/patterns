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



# Pattern - 4: Right-Angled Number Pyramid - II

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def RightNumberPyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=' ')
        print()
            
    
    
    
# RightNumberPyramid(5)


# Pattern-5: Inverted Right Pyramid

# * * *
# * * 
# *

def inverted(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end=' ')
        print()
        

# inverted(5)



# Pattern - 6: Inverted Numbered Right Pyramid


# 1 2 3
# 1 2
# 1

def invertedNumber(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end=' ')
        print()
        
        
# invertedNumber(5)



# Pattern - 7: Star Pyramid

#  *  
# *** 
# *****

def star(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end='')
        for j in range(2*i+1):
            print("*", end='')
        for j in range(n-i-1):
            print(" ",end=' ')
        print()


# star(5)


# Pattern - 8: Inverted Star Pyramid

# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

def InvertedStar(n):
    for i in range(n):
        for j in range(i):
            print(" ", end='')
        for j in range(2*n-(2*i+1)):
            print("*",end='')
        for j in range(i):
            print(" ",end='')
        print()



InvertedStar(5)