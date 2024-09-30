# Given number
base_number = 2
# Length of the list
length = 5

# Create a list of indices
indices = list(range(length))

# Use map to calculate the power of base_number raised to the index
powers = list(map(lambda index: base_number ** index, indices))

# Print the result
print(powers)
