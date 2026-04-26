import sys

type = sys.argv[1]
if type == "t2.micro":
    print("it will charge 2 dollar per day")
elif type =="t2.xlarge":
    print(" it will charge 8 dollars per day")
else:
    print("Please provide a valid type like t2.micro or t2.xlarge")