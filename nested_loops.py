# Nested Loop - Loop is inside another Loop
'''
b = int(input())
for n in range(1, b):
    for i in range(1, 11):
        if n%10 == 0:
            break
        print(n, 'x', i, '=', n*i)
    print('---------------')
'''


'''
*
* *
* * *
* * * *
'''
for i in range(4):
    for j in range(i+1):
        print("*", end = " ")
    print("")


'''
* * * *
* * *
* *
*
'''
for i in range(3, -1, -1):
    for j in range(i+1):
        print("*", end = " ")
    print("")



for i in range(1, 5):    # [1, 2, 3, 4]
    for j in range(5-i):   # [4, 3, 2, 1]
        print("*", end = " ")
    print("")


'''
1
1 2
1 2 3
1 2 3 4
'''
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end = " ")
    print("")

'''
1
2 2
3 3 3
4 4 4 4
'''
for i in range(1, 5):
    for j in range(1, i+1):
        print(i, end = " ")
    print("")

'''
1
2 3
4 5 6
7 8 9 10
'''

k = 1
for i in range(1, 5):
    for j in range(1, i+1):
        print(k, end = " ")
        k = k+1
    print("")

'''
      *
    * *
  * * *
* * * *
'''
for i in range(1, 5):
    for j in range(4-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print("")


'''
* * * *
  * * *
    * *
      *
'''

for i in range(1, 5):
    for j in range(i-1):
        print(" ", end=" ")
    for k in range(5-i):
        print("*", end=" ")
    print("")


'''
      * *
    * * * *
  * * * * * *
* * * * * * * *

A
A B
A B C
A B C D
'''

