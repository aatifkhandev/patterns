# Count digits in a number

# N = 12345           
# Output:5

def count(n):
    count = 0
    while n>0:
        n = n//10
        count = count+1
    print(count)

count(12345)
        