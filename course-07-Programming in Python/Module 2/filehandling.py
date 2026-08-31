# file = open('note.txt',mode='r')
# data = file.readlines()
# print(data)

# #creating with new file

# with open('test.txt','w') as file:
#     file.write('this is just for testing')

with open('test.txt', 'r') as file:
 lines = file.readlines()
print(lines)