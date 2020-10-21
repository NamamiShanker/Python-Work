lis = list(map(int, input().split()))
m = 0

i = 0
while i < len(lis):
    if lis[i] > lis[m]:
        m = i
    i+=1

lis.pop(m)

m = 0
i = 0
while i < len(lis):
    if lis[i] > lis[m]:
        m = i
    i+=1

print(lis[m])


