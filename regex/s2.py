import re

text = "hello World"
pattern = r"hello"
result = re.search(pattern, text)
print(result)

if result:
    print(result.group())