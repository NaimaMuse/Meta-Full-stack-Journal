# two types of KeyError
#   1. SyntaxError   : developer cause 
#   2. Exception KeyError:  maths error

#   1. SyntaxError   :
# name = 'naima'
# if name =="naima"  
#     print('good')


# 2. Exception KeyError
# print(4/0)

# how to handle
def div(a,b):
    return a/b
try:
    answer = div(40,0)
except Exception as e:
    print("something is wrong",e)

