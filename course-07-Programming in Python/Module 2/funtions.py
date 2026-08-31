def calculate_text(bill,textrate):
    return bill * textrate
print(calculate_text(4,5))

# variable global scope
num1 = 4

def sum():
    #local variable
    num1 = 4
    num2 = 5
    return num1 + num2

print(sum())