
strings = ["hello", "world", "python"]

listified_strings = list(map(lambda s: list(s), strings))


print(listified_strings)
