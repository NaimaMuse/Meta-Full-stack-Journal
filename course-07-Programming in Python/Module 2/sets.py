myset1 = {1,2,3,4,5,5}
#set remove duplicates
myset1.add(6) #add
myset1.remove(4)  #remove
myset1.discard(5)   #remove
print(myset1)


myset1 = {1,2,3,4,5,7}
myset2 = {6,7,8,9,0}
# unites and remove duplicates
print(myset1.union(myset2))
print(myset1 | myset2) # same like union

print(myset1.intersection(myset2)) # same value

print(myset1.difference(myset2)) # values that set1 have that set 2 doesnt have
print(myset1 - myset2)  # same like the difference

print(myset1.symmetric_difference(myset2)) # waxa aanay iskaga midka ahayn
print(myset1^myset2) #  same to symmetric_difference

print(myset2[2]) #'set' object is not subscriptable you cant acces the index 
