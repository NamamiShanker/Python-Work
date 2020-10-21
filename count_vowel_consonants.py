'''
s = input("Enter the sentence: ")
vowel = 'aeiou'
spec = '!@#$%^&*()_+{}[]:;<>?,./1234567890'
v = 0
c = 0
for i in s:
    if i in vowel:
        v +=1
        pass
    elif i == ' ':
        print('Space detected')
    elif i in spec:
        print('special char detected')
    else:
        c+=1

print("Total vowels =", v)
print("Total consonants =", c)
'''
# local variable and global variable

def isVowel(i):
    return i in 'aeiou'
def isSpecial(i):
    return i in '!@#$%^&*()_+{}[]:;<>?,./1234567890'
def isSpace(i):
    return i == ' '

s = input("Enter the sentence: ")
v=0
c=0
for k in s:
    if isVowel(k):
        v+=1
    elif not(isSpecial(k) or isSpace(k)):
        c+=1

print("Total vowels =", v)
print("Total consonants =", c)

