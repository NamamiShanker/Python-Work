def factors(a):
    count = 0
    for i in range(1, a+1):
        if a%i == 0:
            count+=1
    return count

def prime(n):
    no_of_factors = factors(n)
    if no_of_factors == 2:
        print("Prime Number")
    else:
        print("Not a prime number")


prime(16)
