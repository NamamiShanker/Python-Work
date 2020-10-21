print("The game starts. Think of a number between 1 and 100")
lower = 1
upper = 100

for i in range(7):
    middle = int((lower+upper)/2)
    val = input("Where you thinking of "+str(middle))
    if val == 'yes':
        print("Number found")
        break
    else:
        val = input("Is your number 'bigger' or 'smaller' than my guess??: ")
        if val == 'bigger':
            lower = middle + 1
        else:
            upper = middle - 1
