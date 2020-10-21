file = open('cars.txt', 'r')
data = file.read()
file.close()

file_copy = open('cars_copy.txt','w')
file_copy.write(data)
file_copy.close()
