
import sys

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    print("=== Addition of Two Numbers ===")
    try:
        if len(sys.argv) == 3:
            # Case 1: Arguments passed (for Jenkins or CLI)
            a = float(sys.argv[1])
            b = float(sys.argv[2])
        else:
            # Case 2: No arguments passed (for console use)
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

        print("\n=== Program Parameters ===")
        print("First Number  :", a)
        print("Second Number :", b)

        result = add_numbers(a, b)
        print(f"\nSum = {result:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
