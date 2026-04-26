import sys

print("Arguments passed:" sys.argv)

script_name = sys.argv[0]
print("Script name:", script_name)

if len(sys.argv) > 1:
    first_argument = sys.argv[1]
    print(first_argument)
else:
    print("No arguments passed")