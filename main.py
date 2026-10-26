
from basic_operations import add, subtract
from advanced_operations import multiply, divide


def main():
    print("\n=== Python Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    else:
        try:
            result = divide(a, b)
        except ValueError as error:
            print("Error:", error)
            return

    print("Result:", result)


if __name__ == "__main__":
    main()
