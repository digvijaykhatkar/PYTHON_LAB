def compute_power(base, exponent):
    return base ** exponent


try:
    x = float(input("Enter the base (X): "))
    n = int(input("Enter the exponent (n): "))
    
    
    result = compute_power(x, n)
    
    
    print(f"The value of {x} raised to the power of {n} is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid number for base and an integer for exponent.")
