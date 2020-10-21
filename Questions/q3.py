def countFactors(n):
    s = 0
    for i in range(1, n+1):
        if n%i==0:
            s+=1
    return s

num = int(input("Enter the number: "))
noOfFacs = countFactors(num)
if noOfFacs == 2:
    print("Prime Number")
else:
    print("Composite Number")
