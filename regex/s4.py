import re

pattern = r"\s+"  # One or more spaces
string = "Python   is    great"
new_string = re.sub(pattern, " ", string)

print(new_string)  # Output: Python is great

