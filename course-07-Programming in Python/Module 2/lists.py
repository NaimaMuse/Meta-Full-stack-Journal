list1 = [1,2,3,4,5]
print(list1[2])
print(*list1)
print(list1,sep=",")

#adding item to the list
list1.insert(len(list1),6)
print(list1,sep=",")

list1.append(7)
print(list1,sep=",")

list1.extend([8,9,10])
print(list1,sep=",")

#delete item from the list
list1.pop()
print(list1,sep=",")
#index
list1.pop(6)
print(list1,sep=",")

del list1[2]
print(list1,sep=",")

# iterate through the lst 
for list in list1:
    print(list)