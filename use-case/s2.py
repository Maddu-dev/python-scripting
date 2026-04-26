import sys

def main():
    try:
        # sys.argv[0] is the script name; [1] and [2] are the arguments
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        
        result = num1 / num2
        
    except IndexError:
        # Occurs if fewer than two arguments are provided
        print("Error: Missing arguments. Provide two numbers.")
        
    except ValueError:
        # Occurs if arguments are not valid numbers (e.g., 'abc')
        print("Error: Arguments must be numeric.")
        
    except ZeroDivisionError:
        # Occurs if the second number is zero
        print("Error: Cannot divide by zero.")
        
    else:
        # Executes ONLY if the try block succeeds without any errors
        print(f"Calculation successful! Result: {result}")
        
    finally:
        # Executes ALWAYS, whether an error occurred or not
        print("Cleaning up resources and exiting script.")

if __name__ == "__main__":
    main()
