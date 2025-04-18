# Print name 5 times


def PrintName(name,count):
    if count == 5:
        return
    print(name)
    count+=1
    PrintName(name,count)
    

PrintName("aatif",0)