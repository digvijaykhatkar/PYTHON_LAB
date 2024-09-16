def is_armstrong_number(number):
  
    num_str = str(number)
    num_digits = len(num_str)
    
   
    total_sum = sum(int(digit) ** num_digits for digit in num_str)
    
 
    return total_sum == number

def print_armstrong_numbers(start, end):
    print(f"Armstrong numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_armstrong_number(number):
            print(number)

print_armstrong_numbers(1, 1000)
