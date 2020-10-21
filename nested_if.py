'''
n = 30

if n>20 and n<40:
    print("It is in the range.")
else:
    print("It is out of the range.")
'''

# Leap year program

year = int(input("Enter the year: "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
    
