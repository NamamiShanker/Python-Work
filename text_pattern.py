'''
TEXT: EDUCATIONAL
PATTERN: DON
YES
'''

text = input("Enter the word: ")
patt = input("Enter the pattern: ")

a = 0      # Keeps track of which letter of pattern we are searching for in text.
flag = False

for letter in text:
    if letter == patt[a]:
        a+=1
        if a == len(patt):
            flag = True
            break

if flag:
    print("YES")
else:
    print("NO")
