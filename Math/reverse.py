# i/p = 7789
# o/p = 9877

def reverse(n):
    revNum = 0
    while(n>0):
        digit = n%10
        n = n//10
        revNum = (revNum*10)+digit
    return revNum





n = int(input("Enter a Number"))
print(reverse(n))