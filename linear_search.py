lis = [4,1,2,3,4,5,6]
val = 4
index = -1
k = 0
for i in lis:
    if val == i:
        index = k
        break
    k+=1
if index == -1:
    print("Not Found!")
else:
    print("Found at", index)
