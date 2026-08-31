tubles1 = (1,2,3,'hi',True)
print(tubles1[2])
print(type(tubles1))
print(tubles1.index(2))
for x in tubles1:
    print(x)

# tubles are immutable that means you cant chnage 
tubles1[3]=5
print(tubles1)