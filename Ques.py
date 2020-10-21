lis = [100,5,70,2]
lis_copy = lis.copy()
lis_copy.sort()

rank = []

def findRank(n): # Linear Search Algorithm
    i = 0
    while i<len(lis_copy):
        if lis_copy[i] == n:
            return i+1
        i+=1
    
for i in lis:
    r = findRank(i)
    rank.append(r)

print(rank)
