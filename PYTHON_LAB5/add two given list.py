
list1 = [10, 20, 30]
list2 = [5, 15, 25]


sum_list = list(map(lambda x, y: x + y, list1, list2))


difference_list = list(map(lambda x, y: x - y, list1, list2))

print("Sum of the lists:", sum_list)
print("Difference of the lists:", difference_list)
