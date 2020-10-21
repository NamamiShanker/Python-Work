n = int(input("Enter the limit: "))

prev = 0
current = 1
nxt = prev + current

if n==1:
    print(prev)

elif n==2:
    print(current)

else:
    for i in range(n - 2):
        nxt = prev + current
        prev = current
        current = nxt
    print(current)

# 0 1 1 2 3 5 8 13 21 34
