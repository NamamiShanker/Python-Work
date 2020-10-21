def convert_to_pig_latin(word):
    start = word[0]
    end = word[1: ]
    join = end + start
    modified = join + 'ay'
    return modified

s = input()
words = s.split()

for word in words:
    modified = convert_to_pig_latin(word)
    print(modified)
