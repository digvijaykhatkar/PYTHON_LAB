def is_harshad_number(number):
  
    num_str = str(number)
    
 
    digit_sum = sum(int(digit) for digit in num_str)
    
   
    return number % digit_sum == 0

number = int(input("Enter a number to check if it's a Harshad number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
