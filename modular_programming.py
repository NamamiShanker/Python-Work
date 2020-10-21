# add, sub, prod, div,

def add(n, m):
    return (n+m)

def sub(n, m):
    return (n-m)

def prod(n, m):
    return (n*m)

def div(n, m):
    return (n/m)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
choice = input("Enter your choice of operation +, -, *, /: ")

if choice == '+':
   ans = add(num1, num2)

elif choice == '-':
   ans = sub(num1, num2)
   
elif choice == '*':
   ans = prod(num1, num2)
   
elif choice == '/':
   ans = div(num1, num2)

else:
    print("Invalid choice")

print(ans)
