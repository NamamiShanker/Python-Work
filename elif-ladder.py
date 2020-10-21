'''
>=90 = A
>=80 , <90 = B
>=70 , <80 = C
>=60 , <70 = D
<60 = F
'''
# 

n = int(input())
if n>=90:
    print("A")
elif 80<=n:
    print("B")
elif 70<=n:
    print("C")
elif 60<=n:
    print("D")
else:
    print("F")
