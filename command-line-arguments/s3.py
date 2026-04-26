import sys

def add(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

def sub(num1, num2):
    return num1 - num2

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == 'add':
    output = add(num1, num2)
    print(output)

elif operator == 'sub':
    output = sub(num1, num2)
    print(output)
else: 
    print("Please give the correct operation, it is ")
