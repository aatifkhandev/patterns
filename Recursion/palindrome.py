def f(i,s):
    if i>=len(s)//2:
        return True
    if s[i]!=s[len(s)-i-1]:
        return False
    return f(i+1,s)

s = "madam"
if f(0,s):
    print("palindrome")
else:
    print("not a palindrome")