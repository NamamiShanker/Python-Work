s = 'ayush'
vowels = ['a', 'e', 'i', 'o', 'u']
count_of_vowels = 0

for char in s:
    flag = False
    # check whether char is a vowel
    for el in vowels:   # Iterating through # vowels list
        if char == el:
            flag = True
            break
    if flag==True:
        count_of_vowels+=1

print(count_of_vowels)
