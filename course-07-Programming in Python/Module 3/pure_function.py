# this is not a pure funtion

mylist = [1,2,3]

def addto_list(item):
    return mylist.append(item)

addto_list(4)
print(mylist)