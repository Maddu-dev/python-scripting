import re
text = "hello world"

pattern = r"hello"

result = re.match(pattern, text)
print(result)

result1 = re.match("google", text)
print(result1)

result2 = re.match("world", text)
print(result2)