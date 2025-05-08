name = "aatif"
def count(counter):
    
    if counter==5:
        return
    print(name)
    count(counter+1)
    
count(0) 



def countTillFour(cnt):
    if cnt==4:
        return
    
    print(cnt)
    # cnt+=1
    countTillFour(cnt+1)
    

countTillFour(0)


# second version of printing name

def nameAgain(i,name):  
    if i>5:
        return
    print(name)
    nameAgain(i+1,name)
    
nameAgain(1,"Aatif")

