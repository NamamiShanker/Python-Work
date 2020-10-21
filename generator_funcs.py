def generator():
    k = 1
    while True:
        yield k*k
        k+=1

for i in generator():
    if i>100:
        break
    print(i)


'''
for i in range(11):
    print(i*i)
numpy, matplotlib, regex, parsing, 
