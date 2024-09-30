
sequence = "Hello World!"


uppercase_letters = list(map(lambda x: x.upper(), set(sequence)))
lowercase_letters = list(map(lambda x: x.lower(), set(sequence)))


uppercase_letters.sort()
lowercase_letters.sort()

print("Uppercase letters:", ''.join(uppercase_letters))
print("Lowercase letters:", ''.join(lowercase_letters))
