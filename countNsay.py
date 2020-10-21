n = int(input())
s = '1' + '0'
for i in range(n):
    current  = s[0]
    count = 0
    snew = ''
    for i in s:
        if i == current:
            count+=1
        else:
            snew = snew+str(count) + current
            current = i
            count = 1
    print(snew)
    s = snew+'0'
