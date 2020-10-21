'''
*
* *
* * *
* * * *

* * * *
* * *
* *
*

      *
    * *
  * * *
* * * *


s = '* '
for i in range(1, 5):
    print(s*i)

for i in range(5, 0, -1):
    print(s*i)

for i in range(1, 5):
    print("  "*(5-i) + (s*i))

for i in range(5, 0, -1):
    print("  "*(5-i) + s*i)
'''
s = '* '

for i in range(1, 5):
    print("  "*(5-i) + 2*s*i)

for i in range(5, 0, -1):
    print("  "*(5-i) + 2*s*i)












