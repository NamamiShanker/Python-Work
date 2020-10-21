y = int(input("Enter the year: "))
if(y%4==0):
    if(y%100 == 0):
        if(y%400 == 0):
            print("It is a special Leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a normal leap year")
else:
    print("Not Leap Year")
