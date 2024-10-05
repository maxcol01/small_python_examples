my_list = [5, 4, 3]

# create lambda expression that will square this !

print(list(map(lambda num: num ** 2, my_list)))

# List sorting: sort the list based on the second value in the tuples item

second_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(second_list, key=lambda item: item[1], reverse=True))
