def is_disarium_number(number):
   
    num_str = str(number)
    
    
    total_sum = 0
    
   
    for i, digit in enumerate(num_str):
        
        power = i + 1  
        digit_value = int(digit)
        total_sum += digit_value ** power
    
    return total_sum == number


number = int(input("Enter a number to check if it's a Disarium number: "))
if is_disarium_number(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")
