# i/p = 371 = 3 cube + 7 cube + 1 cube
# o/p = True

def armstrong(n):
    dup = n
    sum = 0
    while(n>0):
        digit = n%10
        sum = sum+(digit*digit*digit)
        n = n//10
    return dup==sum
        




print(armstrong(34343))