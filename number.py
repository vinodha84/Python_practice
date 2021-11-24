list = []
def number():
    for i in range (2000,3200):
        if (i%7) == 0 and (i%5) != 0:
            list.append(str(i))
            #print("Number is", i)
    return list

list= number() 
print(','.join(list))           