import math

def main():
    try:
        num = float(input("Enter a number: "))
        if num <= 0:
             print("The natural logarithm is undefined for non-positive numbers.")

        sqrt_value = math.sqrt(num)
        log_value = math.log(num) if num > 0 else "undefined"
        sin_value = math.sin(num)

        print(f"Square root of {num}: {sqrt_value}")
        print(f"Natural logarithm of {num}: {log_value}")
        print(f"Sine of {num} (in radians): {sin_value}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ =="__main__":
    main()