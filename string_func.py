s = "abc ABC 123 ?!#"

s_upper = s.upper()
# print(s_upper)

s_lower = s.lower()
# print(s_lower)

# ---------------------------------------------------------------
# List in python                                                #
lis = [ 'GTA V' , 'CSGO' , 'Minecraft' , 'Red Redemption 2' ]   #
# index     0       1           2               3               #
# print(lis)                                                    #
# print( lis[2] ) # indexing                                    #
# ---------------------------------------------------------------


# split()
sentence = "CSGO is more competitive than GTAV"
words = sentence.split()  # split() gives a list of words in the sentence
# print(words)

# strip()
sentence = "     Daubermann Boxer   "
cleaned = sentence.strip()
#print(cleaned)
# print(sentence)

# len() - It is not a string function, finds the length of any sequence
s = "0123456"
l = len(s)
print(l)


