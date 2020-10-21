'''
Question : Given an input number n, write a program that prints a multiplication table for numbers up to n.
'''

# n = 6
limit = int(input("Enter till which number you want to print tables: "))

for n in range(1, limit+1 ):
    print('----------------------')
    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)
