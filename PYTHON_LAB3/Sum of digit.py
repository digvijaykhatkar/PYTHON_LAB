def sum_of_digits(number):
    
    num_str = str(number)
    
   
    digit_sum = sum(int(digit) for digit in num_str)
    
    return digit_sum


try:
    num = int(input("Enter a number to find the sum of its digits: "))
    
    
    result = sum_of_digits(num)
    
    
    print(f"The sum of the digits in {num} is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
