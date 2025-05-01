# i/p = 4554
# o/p = palindrome

# i/p = 7789
# o/p = not a palindrome

def palindrome(n):
    revNum = 0
    duplicate = n
    while n>0:
        digit = n%10
        n = n//10
        revNum = (revNum*10)+digit
    if duplicate == revNum:
        return True
    else:
        return False
        
print(palindrome(4554))