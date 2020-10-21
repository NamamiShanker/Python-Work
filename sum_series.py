n = int(input())
s = 0

for i in range(1, n+1):
    s = s + i

print(s)

# Sum of even numbers

s = 0

for i in range(1, n+1):
    if i%2 == 0:
        s = s + i

print(s)
