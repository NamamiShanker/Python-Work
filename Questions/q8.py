# Fibonacci Series
## 0 1 1 2 3 5 8 13 21 ...
# Make a program that prints the nth number of Fibonacci series

a = 0
b = 1
n = int(input("Enter the limit: "))

if n==1:
    print(a)
elif n==2:
    print(b)
else:
    for i in range(n-2):
        c = a + b
        a = b
        b = c
    print(b)
