# Two ways to traverse a list

# Use the while loop - slower

lis = ["Apple", "Orange", "carrot", "peach", "mushroom"]
'''
While loop traversal
--------------------
i = 0
while i<len(lis):  
    print(lis[i])
    i+=1
'''
# For loop traversal - faster

for i in lis:
    print(i)

