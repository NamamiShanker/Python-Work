# Advanced if else statement - elif ladder
# -----------------------------------------

'''
Banana, Orange, Apple
<=10 w - Banana
>10 and <=20  - Orange
>20 and <=30  - Apple
>30 and <=40  Watermelon
>40 Knife
'''

money = 5

if money<=10:
    print("Banana")
elif money <= 20:
    print("Orange")
elif money <=30:
    print("Apple")
elif money <= 40:
    print("Watermelon")
else:
    print("Knife")
