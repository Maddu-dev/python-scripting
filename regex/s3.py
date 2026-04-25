import re

text = "Hello how are you \
My Name is Maddu Veeranaresh Kumar \
I love Python \
I hope you all are folllowing my lectures and learning Python"

pattern = r"Python"
result = re.findall(pattern, text)
print(result)
result1 = re.search(pattern, text)
print(result1)