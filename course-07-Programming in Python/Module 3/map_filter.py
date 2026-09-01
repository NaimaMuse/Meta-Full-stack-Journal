# # # numbers = [1, 2, 3, 4]

# # # def double(number):
# # #     return number * 2

# # # result = map(double, numbers)

# # # print(list(result))



# # # numbers = [1, 2, 3, 4, 5, 6]

# # # def is_even(number):
# # #     return number % 2 == 0

# # # result = filter(is_even, numbers)

# # # print(list(result))

# # a = [[96], [69]]

# # print(''.join(list(map(str, a))))

# # z = ["alpha","bravo","charlie"]
# # new_z = [i[0]*2 for i in z]
# # print(new_z)

# # def summation(n):
# #    if n == 1:
# #        return 0
# #    return n + summation(n-1)

# # a = summation(5)
# # print(a)

# some = ["aaa", "bbb"]

# #1
# def aa(some):
#    return

# #2
# # def aa(some, 5):
# #    return

# #3
# def aa():
#    return

# #4
# def aa():
#    return "aaa"


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)