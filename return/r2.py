# returning of multiple values

def get_details():
    name = "Jai"
    age = 30
    return name, age

details = get_details()
print(details)

def check_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

result = check_even(5)
result1 = check_even(2)
print(result)
print(result1)