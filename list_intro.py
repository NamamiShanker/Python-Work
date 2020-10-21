cake = [13, 15, 34, 67, 89, 67, 62]
cherry = ["Banana", "Apple", "Cherry", "Mango", "Guava"]

# print(cake)

# Iteration
for i in cake:
    # print(i, end=', ')
    pass

# Max function
print(max(cake))
print(max(cherry))

# Min function
print(min(cake))
print(min(cherry))

# del operator - deletes the elements of a list OR othe whole list
    # del cake[1]
    # print(cake)
# del cake
# print(cake)


# remove function
cake.remove(67)

# len() function
print("Length of cake =", len(cake))
print("Length of cherry =", len(cherry))

# list() - It can convert any sequence into a list
sent = "I love biriyani"
list_alphabets = list(sent)
# print(list(range(1,600)))

# append() - Adds an element to the list at the end
cake.append(79)
cherry.append("Kiwi")

print(cake)
print(cherry)

# clear()
cake.clear()
print(cake)

# copy()
