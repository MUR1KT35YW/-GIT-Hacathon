lst1=['h','y']
lst2=[6,7,8,9,10]
list=[]
def weight(x):
    for i in lst1:
        if(x==i):
            list.append(1)
        else:
            pass
    for i in lst2:
        if(x==i):
            list.append(2)
        else:
            pass
weight('h')
print(list)
