# Pattern - 11: Binary Number Triangle Pattern

# 1
# 01
# 101
# 0101
# 10101

def BinaryPattern(n):
   
    for i in range(n):
        start = 1 if i % 2 == 0 else 0
        
        for j in range(i+1):
            
            print(start,end='')
            start = 1-start
        print()
        


# BinaryPattern(5)


# Pattern - 13: Increasing Number Triangle Pattern

# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11  12  13  14  15
# 16  17  18  19  20  21


def triangle(n):
    num = 1
    for i in range(n):
        for j in range(i):
            
            print(num,end=' ')
            num = num+1
        print()
        
# triangle(5)



# Pattern-13: Increasing Letter Triangle Pattern

# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F

def letters(n):
    for i in range(1,n+1):
        for j in range(i):
              # Print letter starting from 'A' + j
            print(chr(65 + j), end=' ')  # chr(65) is 'A'
        print()
        
        
letters(5)