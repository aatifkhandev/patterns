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
        


BinaryPattern(5)