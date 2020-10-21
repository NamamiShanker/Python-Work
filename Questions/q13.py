# Input: Hello World whats up
# Output: Hello-World-whats-up

# ['Hello', 'World', 'whats', 'up']

s = input()
words = s.split()

snew = ""

for w in words:
    snew = snew + w + '-'
