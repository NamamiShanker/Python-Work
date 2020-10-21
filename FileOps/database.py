# d = {'Name': ['Ninja', 'Manas', 'Tifu', 'MrBeast'], 'Vbucks': [5000, 800, 3000, 8000]}

f = open('table_data.csv', 'r')
c = f.readline().strip() # removing '\n'
columns = c.split(',') # 'columns' is a list containing all the columns categories

d = {}
for i in columns:
    d[i] = []


for i in f:
    row = i.strip().split(',') # A list of all the elements in a row
    counter = 0
    for key in d.keys():
        d[key].append(row[counter])
        counter += 1

print(d)
