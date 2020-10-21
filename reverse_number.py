m = int(input("Enter a number : "))
n = 0
while m!=0:
    dig = m % 10
    m = m//10
    n = n*10 + dig
print(n)
