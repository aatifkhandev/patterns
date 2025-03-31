
count = 0
def printLine(count):
    
    if count >=10:
        return
    count+=1
    
    print(count)
    printLine(count)
    
    
printLine(count)