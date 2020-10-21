def ab_unicode(k = "ABCD"):  # Pasing a value into a function
    name = k
    lis = list(name)
    s = ""
    for i in lis:
        uni = ord(i)
        s = s + str(uni)
    num = int(s)
    numHex = hex(num)
    return numHex

x = ab_unicode('Abhizith')
print(x[2:])
