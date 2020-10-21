lis = [1,4,9,15,19,23,32]
val = 23
index = -1
start = 0
end = len(lis)


while start<=end:
    mid = (start + end)//2
    if lis[mid] == val:
        index = mid
        break
    elif val>lis[mid]:
        start = mid + 1
    else:
        end = mid - 1
        

if index == -1:
    print("Value not found")

else:
    print("Value found at index", index)
