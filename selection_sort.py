lis = [1, 3, 4, 7, 5, 9] # [1, 3, 4, 5, 7, 9]
#      0  1  2  3  4  5  # i =2, smallest_index = 5
i = 0
while i < len(lis):
    j = i
    smallest_index = j
    smallest = lis[j]
    while j < len(lis):
        if lis[j] < smallest:
            smallest = lis[j]
            smallest_index = j
        j+=1
    lis[i], lis[smallest_index] = lis[smallest_index], lis[i]
    i+=1
print(lis)
