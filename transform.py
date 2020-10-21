s = input()
s_new = ""
lis = s.split()
for i in lis:
    first_char = i[0]
    rem_word = i[1:]
    new_word = first_char.upper() + rem_word.lower()
    s_new = s_new + " " + new_word
print(s_new)
